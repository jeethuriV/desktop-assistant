import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import random
import smtplib
import time
import eyed3
from path_required_for_tommy import *

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def take():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        speak("Listening")
        r.pause_threshold=1
        audio = r.listen(source)
    #user=r.recognize_google(audio)
    try:
        print("Recognizing...")
        speak("Recognizing...")
        query=r.recognize_google(audio)
        print("you said: "+query)
        speak("you said: "+query)
        #print(query)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except Exception as e:
        print ("say again")
        return "None"
    return query

if __name__=="__main__":
    
    while 1:
        query=take().lower()  #taking voice query

        if 'open application' in query:
            speak("please specify the application name")
            appname=take()
            #codepath="E:\\Microsoft VS Code\\Code.exe"
            if(appname==code):
                os.startfile(code)
