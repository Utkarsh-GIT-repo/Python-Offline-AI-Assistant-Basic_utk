import pyttsx3
import speech_recognition as sr
from speech_recognition import Recognizer


def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def listen():
    recognize = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listning...")
        audio = recognize.listen(source)
        try:
            command = recognize.recognize_google(audio)
            print(f"You said: {command}")
            return command
        except:
            print("Sorry, I did not understand")
            return None

speak("Hello! How can I help you today?")


def interact():
    user_command = listen()
    if user_command:
        if user_command:
            if "hello" in user_command.lower():
                speak("Hi there! Nice to meet you.")
                interact()
            elif "bye" or "by" in user_command.lower():
                speak("Goodbye!")
            else:
                speak("I am not sure how to respond to that.")
interact()
