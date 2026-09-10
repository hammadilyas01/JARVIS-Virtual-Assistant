import speech_recognition as sr
import webbrowser
import multiprocessing
import wikipediaapi

wiki = wikipediaapi.Wikipedia(
    user_agent="JARVISassistant/1.0 (hammadilyas2001@gmail.com)",
    language="en"
)

def get_wiki_summary(query, sentences=2):
    page = wiki.page(query)
    if page.exists():
        # Take first N sentences from the summary
        text = page.summary
        return ". ".join(text.split(". ")[:sentences]) + "."
    return None

def _speak_worker(text):
    import pyttsx3
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def speak(text):
    p = multiprocessing.Process(target=_speak_worker, args=(text,))
    p.start()
    p.join()


sites = {
    "facebook": "https://www.facebook.com",
    "youtube": "https://www.youtube.com",
    "google": "https://www.google.com",
    "gmail": "https://mail.google.com",
    "instagram": "https://www.instagram.com",
    "github": "https://www.github.com",
    "linkedin": "https://www.linkedin.com",
}

def processCommand(c):
    c = c.lower()
    print("Command: ", c)
    matched = False
    if c.startswith('open'):
        for site, url in sites.items():
            if site in c:
                speak(f"Opening {site}") 
                webbrowser.open(url)
                matched = True
                break

        if not matched:
            target = c.replace("open", "").strip()
            if target:
                speak(f"Opening {target}")
                webbrowser.open(f"https://www.{target}.com")
            else:
                speak("Sorry, I don't know what to open.")


    elif "who is" in c or "what is" in c or "tell me about" in c:
        query = c.replace("who is", "").replace("what is", "").replace("tell me about", "").strip()
        print("Searching Wikipedia for:", repr(query))
        summary = get_wiki_summary(query)
        if summary:
            print(summary)
            speak(summary)
        else:
            speak("I couldn't find a Wikipedia page for that.")
        

    elif c.startswith("search for") or c.startswith("search") or c.startswith("google"):
        query = c.replace("search for", "").replace("search", "").replace("google", "").strip()

        if query:
            speak(f"Searching for {query}")
            webbrowser.open(f"https://www.google.com/search?q={query}")
        else:
            speak("What would you like me to search for?")

    else:
        speak(f"Searching Google for {c}")
        webbrowser.open(f"https://www.google.com/search?q={c}")

if __name__ == "__main__":
    speak("Hi Sir, How can i help you today.")
    while True:
        # listening for wake word 'Jarvis'
        # obtaining audio from the microphone
        r=sr.Recognizer()
        
        print('Recognizing...')
        try:
            with sr.Microphone() as source:
                print('Listening...')
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
            word = r.recognize_google(audio)
            if (word.lower() == 'jarvis'):
                speak('Yes Sir')
                # Listen for command
                with sr.Microphone() as source:
                    r.adjust_for_ambient_noise(source, duration=0.5)
                    print('Jarvis active..')
                    audio = r.listen(source, phrase_time_limit=6)
                    command = r.recognize_google(audio)
                    # Exit condition 
                if command.lower() in ("stop", "end", "quit", "exit", "goodbye"):
                    speak("Goodbye Sir")
                    break

                processCommand(command)
        except sr.WaitTimeoutError:
            print("No speech detected, still listening...")
        except sr.UnknownValueError:
            print("Couldn't understand audio, try speaking clearer/louder")
        except sr.RequestError as e:
            print("Could not reach Google API:", e)
            speak("Could not reach Google API:", e)
        except Exception as e:
            print("Other error:", e)
        
    print("Jarvis has stopped.")