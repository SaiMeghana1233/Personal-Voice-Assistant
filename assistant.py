import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os

# Initialize text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

        try:
            command = r.recognize_google(audio)
            print("You:", command)
            return command.lower()
        except:
            speak("Sorry, I didn't understand")
            return ""

# Start assistant
speak("Hello! I am your assistant")

while True:
    command = listen()

    if "time" in command:
        time = datetime.datetime.now().strftime("%H:%M")
        speak("The time is " + time)

    elif "date" in command:
        date = datetime.datetime.now().strftime("%d %B %Y")
        speak("Today's date is " + date)

    elif "day" in command:
        day = datetime.datetime.now().strftime("%A")
        speak("Today is " + day)

    elif "open google" in command:
        webbrowser.open("https://www.google.com")

    elif "open youtube" in command:
        webbrowser.open("https://www.youtube.com")

    elif "open linkedin" in command:
        webbrowser.open("https://www.linkedin.com")

    elif "open gmail" in command:
        webbrowser.open("https://mail.google.com")

    elif "search" in command:
        query = command.replace("search", "")
        webbrowser.open(f"https://www.google.com/search?q={query}")

    elif "open notepad" in command:
        os.system("notepad")

    elif "open calculator" in command:
        os.system("calc")

    elif "who are you" in command:
        speak("I am your personal voice assistant")

    elif "how are you" in command:
        speak("I am doing great, thank you")

    elif "joke" in command:
        speak("Why did the programmer quit his job? Because he didn't get arrays")

    elif "exit" in command or "stop" in command:
        speak("Goodbye!")
        break

    else:
        speak("Command not recognized")