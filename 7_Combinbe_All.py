import pyttsx3
import speech_recognition as sr
import os
import datetime

username = ""
welcome_counter = 1
intro = "Hi there! what may I call you?"

def speak(text):
    welcome = pyttsx3.init()
    print(text)
    welcome.say(text)
    welcome.runAndWait()
    # if "bye" in text:
    #     return 0
    # else:
    #     capture_user_input()

def welcome(name):
    global username
    username = name
    speak(f"Hi {username} how may I help you today?")


def capture_user_input():
    global welcome_counter
    recognize_voice = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listning...")
    try:
        audio = recognize_voice.listen(source)
        command = recognize_voice.recognize_google(audio)

        if welcome_counter == 1:
            welcome_counter += 1
            welcome(command)
        elif "bye" in command.lower():
            speak("Goodbye! Have a great day!")
            return False
        else :
            speak(f"Did you say {command}?")
        return True
    except sr.UnknownValueError:
        speak("Sorry I didn't get that")
        return True

speak(intro)
while capture_user_input():
    pass