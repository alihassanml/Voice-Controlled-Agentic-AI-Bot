import os
import time
import threading
import speech_recognition as sr

recognizer = sr.Recognizer()
stop_speech_event = threading.Event()
listening_active = True
last_speech_time = time.time()  

def listen():
    global listening_active, last_speech_time

    with sr.Microphone() as source:
        print("🎤 Listening...")
        recognizer.adjust_for_ambient_noise(source)
        while listening_active:
            try:
                audio = recognizer.listen(source, timeout=3)  
                stop_speech_event.set()
                user_query = recognizer.recognize_google(audio)
                print(f"🗣 User: {user_query}")
                last_speech_time = time.time()  

            except (sr.UnknownValueError, sr.RequestError, sr.WaitTimeoutError) as e:
                print(f"⚠ Error: {e}")
                stop_speech_event.clear()

            if time.time() - last_speech_time > 3:
                print("⏸️ No speech detected for 3 seconds, stopping...")
                stop_speech_event.clear()
def main():
    threading.Thread(target=listen, daemon=True).start()
    
    while True:
        time.sleep(1)

if __name__ == "__main__":
    main()
