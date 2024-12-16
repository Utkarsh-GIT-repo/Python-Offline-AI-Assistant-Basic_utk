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
    if "bye" in text:
        return 0
    else:
        capture_user_input()

def welcome(hi):
    username = hi
    speak("Hi " + username + "how may I help you today?")


def capture_user_input():
    global welcome_counter
    recognize_voice = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listning...")
        audio = recognize_voice.listen(source)
    try:
        command = recognize_voice.recognize_google(audio)
        if "bye" in command:
            speak(command)
        elif welcome_counter == 1:
            welcome_counter += 1
            welcome(command)
        else :
            speak("Did you say " + command)
        return command
    except Exception as e:
        speak("Sorry I didn't get that")




speak(intro)