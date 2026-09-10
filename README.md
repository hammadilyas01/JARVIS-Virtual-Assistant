# 🤖 JARVIS Voice Assistant

A simple Python-based **Voice Assistant** that can listen to voice commands and perform different tasks such as opening websites, searching Google, and getting information from Wikipedia.

This project uses **Speech Recognition**, **Text-to-Speech**, **Wikipedia API**, and Python's built-in web browser functionality.

---

## ✨ Features

* 🎤 Voice recognition using microphone
* 🤖 Wake word detection using **"Jarvis"**
* 🔊 Text-to-Speech responses
* 🌐 Open popular websites using voice commands
* 🔍 Search anything on Google
* 📚 Get information from Wikipedia
* 🛑 Stop the assistant using voice commands
* 🎙️ Ambient noise adjustment for better voice recognition

---

## 🛠️ Technologies Used

* Python
* SpeechRecognition
* PyAudio
* pyttsx3
* Wikipedia API
* multiprocessing
* webbrowser

---

## 📂 Project Structure

```text
JARVIS-Voice-Assistant/
│
├── main.py
├── README.md
├── requirements.txt
└── .gitignore
```

---

## 📦 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/JARVIS-Voice-Assistant.git
```

### 2. Open the Project Folder

```bash
cd JARVIS-Voice-Assistant
```

### 3. Create a Virtual Environment

```bash
python -m venv env
```

### 4. Activate the Virtual Environment

#### Windows PowerShell

```bash
env\Scripts\Activate.ps1
```

#### Windows Command Prompt

```bash
env\Scripts\activate
```

---

## 📥 Install Required Libraries

Install all required Python libraries using:

```bash
pip install -r requirements.txt
```

Or install them manually:

```bash
pip install SpeechRecognition
pip install pyttsx3
pip install wikipedia-api
pip install PyAudio
```

---

## ▶️ How to Run the Project

After activating the virtual environment, run:

```bash
python main.py
```

JARVIS will greet you and start listening for the wake word:

```text
Jarvis
```

After saying **Jarvis**, you can give a command.

---

## 🎙️ Available Voice Commands

### Open Websites

You can say:

```text
Jarvis
Open YouTube
```

```text
Jarvis
Open Google
```

```text
Jarvis
Open Facebook
```

```text
Jarvis
Open GitHub
```

```text
Jarvis
Open LinkedIn
```

### Search Google

You can say:

```text
Jarvis
Search Python tutorials
```

or:

```text
Jarvis
Google artificial intelligence
```

### Search Wikipedia

You can say:

```text
Jarvis
Who is Elon Musk
```

```text
Jarvis
What is Artificial Intelligence
```

```text
Jarvis
Tell me about Python
```

JARVIS will search Wikipedia and speak a short summary.

### Stop JARVIS

You can stop the assistant by saying:

```text
Stop
```

or:

```text
Exit
```

or:

```text
Goodbye
```

---

## 🌐 Supported Websites

Currently, JARVIS can open:

* Facebook
* YouTube
* Google
* Gmail
* Instagram
* GitHub
* LinkedIn

You can easily add more websites inside the `sites` dictionary in the Python code.

---

## ⚙️ How It Works

### 1. Wake Word Detection

The program continuously listens for the word:

```text
Jarvis
```

### 2. Command Listening

After detecting the wake word, JARVIS listens for the user's command.

### 3. Command Processing

The assistant checks whether the command is related to:

* Opening a website
* Searching Google
* Searching Wikipedia
* Stopping the assistant

### 4. Voice Response

JARVIS uses `pyttsx3` to respond using text-to-speech.

---

## 📚 Python Libraries Used

### SpeechRecognition

Used to recognize voice commands from the microphone.

```python
import speech_recognition as sr
```

### pyttsx3

Used to convert text into speech.

```python
import pyttsx3
```

### wikipedia-api

Used to search and retrieve information from Wikipedia.

```python
import wikipediaapi
```

### webbrowser

Used to open websites and Google searches.

```python
import webbrowser
```

### multiprocessing

Used to run the speech function in a separate process.

```python
import multiprocessing
```

---

## ⚠️ Common Issues

### PyAudio Installation Problem

If you face problems installing PyAudio on Windows, try upgrading pip first:

```bash
python -m pip install --upgrade pip
```

Then try:

```bash
pip install pipwin
pipwin install pyaudio
```

### Microphone Not Working

Make sure:

* Your microphone is connected.
* Microphone permissions are enabled.
* The correct microphone is selected in Windows.
* PyAudio is installed correctly.

---

## 🚀 Future Improvements

Some features that can be added in the future:

* 🤖 AI chatbot integration
* 🌦️ Weather information
* 📰 Latest news
* 🎵 Play music
* 💻 Open applications
* 📧 Send emails
* ⏰ Set reminders and alarms
* 🧠 Memory system
* 💬 Integration with an AI API
* 🔥 Better wake word detection

---

## 👨‍💻 Author

**Hammad Ilyas**

Computer Science Student | Python Learner | AI & Computer Vision Enthusiast

* GitHub: https://github.com/hammadilyas01
* LinkedIn: www.linkedin.com/in/hammad-ilyas-3a883b201

---

## 📄 License

This project is created for learning and educational purposes.

Feel free to use and improve it.

---

⭐ If you like this project, don't forget to give it a star!
