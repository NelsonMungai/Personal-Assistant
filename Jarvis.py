import pyttsx3
from decouple import config

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

speak("HELLO"+USERNAME+"my name is "+BOTNAME+"and am your personal assistant")