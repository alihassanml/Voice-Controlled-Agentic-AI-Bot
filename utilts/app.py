import os
import time
import threading
import json
import requests
import speech_recognition as sr
import subprocess
import playsound

# === MODEL CONFIG ===
model = "llama3.2:1b"  # or "deepseek-coder:6.7b" etc.

# === SETUP ===
recognizer = sr.Recognizer()
stop_speech_event = threading.Event()
listening_active = True
last_speech_time = time.time()
context = None  # For preserving chat history

# === TEMPLATE ===
TEMPLATE = """
You are a smart and thoughtful assistant trained by Ali Hassan.
-If the user greets (e.g., says "hi", "hello"), reply with a short friendly greeting (e.g., "Hi there!").
- Otherwise, directly answer their question.
- Answer in 1–3 short, clear sentences — like a human would.
- Focus only on what the user asks. Do not explain your role or add extra info.
- Always be concise, helpful, and conceptually accurate.
- Provide short, direct, and conceptually rich answers.
- Focus only on what the user asks — no extra info.
- Never mention you are an AI or describe your capabilities.
- Keep responses under 3 clear sentences.
- Prioritize depth of thought and usefulness in minimal words.

User Question: {query}
"""

piper_model_path = "piper/model/en_US-ljspeech-high.onnx"
audio_output_path = "output.mp3"


# === Piper Synth ===
def synthesize_with_piper(text, model_path, output_path="output.mp3"):
    command = [
        "./piper/piper", 
        "--model", model_path,
        "--output_file", output_path
    ]
    process = subprocess.Popen(command, stdin=subprocess.PIPE)
    process.communicate(input=text.encode())


# === Generate Response from Ollama ===
def generate(prompt, context):
    final_prompt = TEMPLATE.format(query=prompt)
    payload = {
        "model": model,
        "prompt": final_prompt,
    }
    if context:
        payload["context"] = context

    r = requests.post("http://localhost:11434/api/generate", json=payload, stream=False)
    r.raise_for_status()

    full_response = ""

    for line in r.iter_lines():
        if not line:
            continue
        body = json.loads(line)
        if "response" in body:
            response_part = body["response"]
            full_response += response_part

        if body.get("done", False):
            context = body.get("context", [])
            break

    # Text-to-speech

    if full_response.strip():
        synthesize_with_piper(full_response, piper_model_path, audio_output_path)
        threading.Thread(target=playsound.playsound, args=(audio_output_path,), daemon=True).start()
        print(f"🤖 {full_response}")


    return context


# === Listen to Mic ===
def listen():
    global listening_active, last_speech_time, context

    with sr.Microphone() as source:
        print("🎤 Listening...")
        recognizer.adjust_for_ambient_noise(source)
        while listening_active:
            try:
                audio = recognizer.listen(source, timeout=3)
                stop_speech_event.set()
                user_query = recognizer.recognize_google(audio)
                print(f"\n🗣 User: {user_query}")
                print("🤖 AI: ", end='')

                context = generate(user_query, context)

                last_speech_time = time.time()
            except (sr.UnknownValueError, sr.RequestError, sr.WaitTimeoutError) as e:
                print(f"⚠ Error: {e}")
                stop_speech_event.clear()

            if time.time() - last_speech_time > 30:
                print("⏸️ No speech detected for 30 seconds. Stopping...")
                listening_active = False
                break


# === Main ===
def main():
    print("🔁 Starting Voice AI with Piper + Ollama...")
    threading.Thread(target=listen, daemon=True).start()

    try:
        while listening_active:
            time.sleep(1)
    except KeyboardInterrupt:
        print("🛑 Interrupted. Exiting...")
        exit()

if __name__ == "__main__":
    main()
