import speech_recognition as sr

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listning...')
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print(f'You said: {command}')
        return command
    except Exception as e:
        print("Sorry, I could not understand.")
        return None

listen()