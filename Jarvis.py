import pyaudio
import pyttsx3
from decouple import config
from datetime import datetime
import speech_recognition as sr
from random import choice
from utils import opening_text

USERNAME=config("USERNAME")
BOTNAME=config("BOTNAME")

print(USERNAME)
print(BOTNAME)

engine=pyttsx3.init()

# setrate 
engine.setProperty("rate",160)

# set volume
engine.setProperty("volume",1.0)

# set Voice(male)
voices=engine.getProperty("voices")
engine.setProperty("voice",voices[74].id)

# print(len(voices))
 
# enable the speak function
def speak(text):
    # used to speak whatever text is passed to it
    engine.say(text)
    engine.runAndWait()

# speak("HELLO Jay, my name is "+BOTNAME+"and am your personal assistant")

# enable the greet function
def greet_user():
    # greeting accoring to time
    hour=datetime.now().hour
    if(hour>=6) and(hour<12):
        speak(f"Good morning {USERNAME}")
    elif(hour>=12) and (hour<16):
        speak(f"Good afternoon {USERNAME}")
    elif(hour>16) and (hour<19):
        speak(f"Good evening {USERNAME}")
    speak(f"I am {BOTNAME}. How may I assist You?")
    speak(f"Goodnight {USERNAME}")

greet_user()

# RECOGNISE USER INPUT
def take_user_input():
    # using SpeechRecognition module
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening....")
        r.pause_threshold=1
        audio=r.listen(source)

    try:
        print("Recognising....")
        query=r.recognize_google(audio,language="en-in")
        if not 'exit' in query or 'stop' in query:
            speak(choice(opening_text))

        else:
            hour=datetime.now().hour
            if hour>=21 and hour < 6:
                speak("Good night sir, take care!")

            else:
                speak("Have a good day sir!")

            exit()


    except Exception:
        speak("Sorry, I could not understand. Could you please say that again?")
        query=None
    return query

take_user_input()