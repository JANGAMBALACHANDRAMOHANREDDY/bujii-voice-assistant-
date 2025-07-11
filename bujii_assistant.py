import speech_recognition as sr
from gtts import gTTS
import pygame
import webbrowser
import os
import random
import difflib

# 🎙️ Text-to-Speech Function
def speak(text):
    print("🗣️ Bujii:", text)
    filename = f"bujii_voice_{random.randint(1000,9999)}.mp3"
    tts = gTTS(text=text, lang='en', tld='co.in')
    tts.save(filename)

    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    pygame.mixer.quit()
    try:
        os.remove(filename)
    except:
        pass

# 🎧 Voice Recognition Function
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎧 Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio).lower()
        print("👤 You said:", command)
        return command
    except:
        return ""

# 🧠 Command Processing
def process_command(command):
    if "open youtube" in command:
        speak("Opening YouTube.")
        webbrowser.open("https://www.youtube.com")
    elif "open google" in command:
        speak("Opening Google.")
        webbrowser.open("https://www.google.com")
    elif "exit" in command or "bye" in command:
        speak("Goodbye! See you later.")
        exit()
    else:
        speak("Sorry, Bujii doesn't understand that command.")

# 🔁 Main Wake Word Loop
def main():
    speak("Bujii is awake. Say 'Hey Bujii' to begin.")
    while True:
        wake = listen()
        wake_words = ["hey bujii", "hi bujii", "hello buji", "hey buji"]
        match = difflib.get_close_matches(wake, wake_words, n=1, cutoff=0.6)

        if match:
            speak("Yes, Bujii is listening.")
            command = listen()
            if command:
                process_command(command)
        else:
            print("🕑 Waiting for wake word...")

# 🚀 Start Bujii
if __name__ == "__main__":
    main()
