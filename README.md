# 🧠🎙️ Voice-Controlled Agentic AI Bot

A real-time voice assistant powered by **Ollama**, **Piper TTS**, and **SpeechRecognition**. This agent listens to voice input, processes it using an LLM, and responds back with natural synthesized speech.

---

## 🚀 Features

- 🎤 Real-time voice input using `SpeechRecognition`
- 🧠 LLM-powered response generation with [`Ollama`](https://ollama.com/)
- 🔊 Text-to-speech output via `Piper`
- 🧵 Multi-threaded performance for responsiveness
- 🧠 Maintains short-term conversation context

---

## 🛠️ Tech Stack

| Component        | Tech                          |
|------------------|-------------------------------|
| Language Model   | `Ollama` (e.g., gemma, deepseek) |
| Voice Recognition| `speech_recognition` + Google API |
| Text-to-Speech   | [`Piper`](https://github.com/rhasspy/piper) |
| Backend Threads  | `Python`, `Threading`         |

---

## 📦 Installation

```bash
# Clone the repo
git clone https://github.com/alihassanml/Voice-Controlled-Agentic-AI-Bot.git
cd Voice-Controlled-Agentic-AI-Bot

# (Optional) Create a virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt
```

---

## 🧪 Run the Bot

> Ensure Ollama is running locally and a model (e.g., `gemma:2b`) is pulled.

```bash
# Start your local Ollama instance
ollama serve

# Pull a model
ollama pull gemma:2b

# Run the bot
python app.py
```

---

## 📁 Directory Structure

```
📦 Voice-Controlled-Agentic-AI-Bot
├── piper/                         # Piper TTS binary and models
├── output.mp3                     # TTS output file
├── app.py                         # Main application
├── requirements.txt               # Python dependencies
└── README.md                      # Project documentation
```

---

## 🔊 Voice Models

Download Piper models from: [https://huggingface.co/rhasspy/piper-voices](https://huggingface.co/rhasspy/piper-voices)

Recommended: `en_US-kristin-medium.onnx`

Place the `.onnx` model under `piper/model/`.

---

## 🧠 Example Interaction

```text
🎤 Listening...

🗣 User: What's the weather in Paris today?
🤖 AI: I'm not connected to real-time data, but Paris is typically mild in April.
```

---

## 📌 To-Do / Enhancements

- [ ] Add wake word detection
- [ ] Integrate GUI interface
- [ ] Add multi-language support
- [ ] Improve context memory window

---

## 👨‍💻 Author

**Ali Hassan**  
[GitHub](https://github.com/alihassanml) | [LinkedIn](https://linkedin.com/in/alihassanml)

---

## 🪪 License

MIT License – use freely, give credit!
