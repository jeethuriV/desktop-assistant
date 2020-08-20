import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import random
import smtplib

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
        r.pause_threshold=1
        audio = r.listen(source)
    #user=r.recognize_google(audio)
    try:
        print("Recognizing...")
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

def getListOfFiles(dirName):
    # create a list of file and sub directories 
    # names in the given directory 
    listOfFile = os.listdir(dirName)
    allFiles = list()
    # Iterate over all the entries
    for entry in listOfFile:
        # Create full path
        fullPath = os.path.join(dirName, entry)
        # If entry is a directory then get the list of files in this directory 
        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(fullPath)
        else:
            allFiles.append(fullPath)
                
    return allFiles        

def askpath():
    path=input("enter the folders path")
    return path


if __name__=="__main__":
    if 1:
        query=take().lower()
        if 'play music' in query:
            #main()
            dirName = askpath()
            listOfFiles = getListOfFiles(dirName)
            for elem in listOfFiles:
                print(elem)
            print ("#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#")
            listOfFiles = list()
            for (dirpath, dirnames, filenames) in os.walk(dirName):
                listOfFiles += [os.path.join(dirpath, file) for file in filenames if file.endswith('.mp3')]
            for elem in listOfFiles:
                print(elem)

            if 'randomly' in query:
                j=random.randint(0,len(listOfFiles)-1)
                os.startfile(os.path.join(dirName,listOfFiles[j]))
            else:
                for j in range(0,len(listOfFiles)-1):
                    os.startfile(os.path.join(dirName,listOfFiles[j]))
                    


