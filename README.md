# 📚 Project Documentation: Voice-Controlled Agentic AI Bot (Free Version)

---

## 1. Project Title:
**Voice-Controlled Agentic AI Bot using Open Source APIs**

---

## 2. Project Objective:
To build an **AI assistant** that listens to the user’s voice, understands natural language commands, performs real-world tasks (search, weather, alarms, FAQs), and responds **intelligently** — **without paid APIs**.

---

## 3. Key Features:
- 🎤 **Voice Recognition**: Convert user speech to text.
- 🧠 **Task Reasoning**: Understand the command and select appropriate action (search, set alarm, etc.).
- 🛠️ **Tool Usage**: Automatically call APIs based on need (weather, Wikipedia search, etc.).
- 🔊 **Voice Output**: Bot speaks back the result (optional but impressive).

---

## 4. Architecture Diagram:

```
[User Voice] → [Speech-to-Text] → [AI Reasoning Agent] → [Tool/API Call] → [Result] → [Text-to-Speech]
```

Simple, modular, and easy to extend later.

---

## 5. Requirements (All Free):

| Purpose | Tool/Library | Notes |
|:---|:---|:---|
| Speech-to-Text | **OpenAI Whisper (Free model)** or **Vosk** (completely offline) | No cost |
| Reasoning | **LangChain** (Free) or basic Python code | For handling logic |
| LLM | **Groq LLaMA 3 free trial** or **Local open-source models** | No billing if smartly used |
| Backend Server | **FastAPI** | Free lightweight Python framework |
| Text-to-Speech | **pyttsx3** (offline TTS) or **gTTS** (Google free TTS) | Optional for voice output |
| Others | **Requests**, **uvicorn**, **openai** (for Whisper) | Free |

---

## 6. Full Tools List:
- Python 3.10+  
- FastAPI  
- OpenAI Whisper (small model) or Vosk for offline speech recognition  
- LangChain (for agentic workflows)  
- Pyttsx3 (Text to Speech)  
- Requests (for calling APIs like weather, news)  
- Uvicorn (to run FastAPI server)
- Optional: Groq SDK (if you want ultra-fast LLMs)

---

## 7. MCP (Minimal Complete Project):
Build the **simplest version first** in this order:

1. 🎤 **Take voice input** ➔ convert to text.
2. 🧠 **Detect** what user wants (search, weather, etc.).
3. 🛠️ **Call appropriate API** (example: openweathermap.org for weather).
4. 🗣️ **Speak back result** (or show on screen).

---
## 8. Step-by-Step Development Plan (Roadmap):

| Step | Description | Libraries |
|:---|:---|:---|
| 1 | Set up Python project, install FastAPI, Uvicorn | `pip install fastapi uvicorn` |
| 2 | Implement Speech-to-Text using Whisper (free model) | `pip install openai-whisper` |
| 3 | Build a simple FastAPI server to accept voice | FastAPI, uvicorn |
| 4 | Use LangChain to build a basic "agent" | `pip install langchain` |
| 5 | Connect the agent with Open Weather API, Wikipedia API | Requests |
| 6 | Respond back with text or Text-to-Speech using pyttsx3 | `pip install pyttsx3` |
| 7 | Test with multiple commands and polish it |

---

## 9. External Free APIs You Can Use:
- 🌦️ [OpenWeatherMap Free API](https://openweathermap.org/api)
- 📖 [Wikipedia Python API](https://pypi.org/project/wikipedia/)
- 📰 [NewsAPI Free Plan](https://newsapi.org/)

---

## 10. Folder Structure:

```
voice_agentic_ai/
│
├── app.py (FastAPI backend)
├── agent.py (LangChain agent logic)
├── speech_to_text.py (Whisper/Vosk STT)
├── text_to_speech.py (pyttsx3 TTS)
├── tools/
│   ├── weather.py
│   ├── search.py
├── requirements.txt
```

---

## 11. Example Commands Bot Can Handle:
- "What's the weather today?"
- "Search for benefits of drinking green tea."
- "Set an alarm for tomorrow 8 AM." (simple mockup)
- "Tell me today's news headlines."

---

## 12. Example Python Requirements (requirements.txt):

```txt
fastapi
uvicorn
openai-whisper
pyttsx3
langchain
requests
wikipedia
```

All these libraries are free, lightweight, and easy to install.

---

# ✅ Summary

You will build a **Voice AI Assistant** that:
- Listens to you (speech recognition)
- Understands you (agent + logic)
- Acts on your command (API calls)
- Talks back to you (text-to-speech)

🌟 **MCP ensures you have a working system fast, and you can expand later.**

