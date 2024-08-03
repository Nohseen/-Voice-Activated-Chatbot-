import speech_recognition as sr  # 'version3.8.1'
import pyttsx3  # 'version2.90'
import pywhatkit  # 'version 3.8'
import datetime  # 'Inbuilt python library'
import wikipedia  # '1.4.0'

listener = sr.Recognizer()  # 'Instance of Recognizer Class'
engine = pyttsx3.init()
engine.say('I am ON')
engine.say('Processing Your Command')


def talk(text):  # 'to talk our command'
    engine.say(text)
    engine.runAndWait()


def take_command():  # 'to input our command'
    command = ""
    try:
        with sr.Microphone() as source:
            print("Listening...\n")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)  # 'google api return a string which will become our command.'
            command = command.lower()  # 'command in lower case for the below 'if' condition to check for 'Alexa' Word.'
            if 'alexa' in command:
                command = command.replace('alexa', '')
    except:
        pass
    return command


def works():  # 'To carry out different work'
    command = take_command()
    print("Your Command : "+command)
    if 'play' in command:
        song = command.replace('play', '')
        talk("Playing"+song)
        print("Playing"+song)
        pywhatkit.playonyt(song)

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk("Current time is "+time)

    elif 'tell me something' or 'give information' in command:
        info = command.replace('tell me something' or 'give information', '')
        result = wikipedia.summary(info, 2)
        print(result)
        talk(result)

    else:
        talk('Please repeat the command.')


works()