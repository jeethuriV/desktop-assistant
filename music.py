import speech_recognition as sr
import pyttsx3
import datetime
import time
import wikipedia
import webbrowser
import os
import random
import smtplib
import eyed3
from path_required_for_tommy import dirName 

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
        speak("Listening...")
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

def askpath():# asks path of the mp3 files located folder in a drive
    path=input("enter the folder path: ")
    return path

def playoff(t):#plays mp3 and display name time period
    os.startfile(os.path.join(dirName,listOfFiles[t]))
    length_in_sec=mp3len(os.path.join(dirName,listOfFiles[t]))
    mins,hours=mp3leninhm(length_in_sec)
    print("\n\n\t", os.path.join(dirName,listOfFiles[t]))
    print("Hours:", hours)
    print("Minutes:", mins)
    print(length_in_sec)
    time.sleep(length_in_sec)
    print ("\n\t*****#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*****\n")
    return 1

def mp3len(t):# mp3 length in seconds
    duration = eyed3.load(t).info.time_secs
    return duration

def mp3leninhm(seconds): # mp3 length in hours and mins
    mins = seconds / 60
    hours= seconds/3600
    return mins,hours

if __name__=="__main__": # execution starts here
    while 1:
        query=take().lower() #taking voice query
        if 'play music' in query: #if the query is play music
            
            if(not(os.path.exists(dirName))):
                print("please enter valid folder path: ")
                dirName = askpath() #"D:\\My MUSIC\\7th Sense"#askpath()
                
            listOfFiles = getListOfFiles(dirName) # loading all the file in folder and its sub folder
            for elem in listOfFiles:
                print(elem)
            print ("\n\t*****#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*****\n")
            listOfFiles = list() #prints path of loaded all the file in folder and its sub folder
            for (dirpath, dirnames, filenames) in os.walk(dirName):
                listOfFiles += [os.path.join(dirpath, file) for file in filenames if file.endswith('.mp3')]
            for elem in listOfFiles:
                print(elem)

            if 'randomly' in query:# plays music randomly and waits for that duration
                for j in range(0,len(listOfFiles)-1):
                    p=random.randint(0,len(listOfFiles)-1)
                    t=p
                    playoff(t)
            else:# plays music from 1 to nth file and waits for that duration
                for j in range(0,len(listOfFiles)-1):
                    t=j
                    playoff(t)
                    


