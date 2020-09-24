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
from path_required_for_tommy import dirName

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def wish(): #wishes like good morning /afternoon/evening 
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        print("Good Morning!")
        speak("Good Morning!")
    elif hour>=12 and hour<=18:
        print("Good Afternoon!")
        speak("Good Afternoon!")
    else:
        print("Good Evening!")
        speak("Good Evening!")
    print("i am your system assistant, How can i help you!")
    speak("i am your system assistant, How can i help you!")

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
    path=input("enter the folder path :")
    return path

def mp3len(t):# mp3 length in seconds
    duration = eyed3.load(t).info.time_secs
    return duration

def mp3leninhm(seconds): # mp3 length in hours and mins
    mins = seconds / 60
    hours= seconds/3600
    return mins,hours

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

def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    speak("please say login email address ")
    #your_email="jeethurivishnu@gmail.com"#take()
    server.login('your_email','your password')#sending address details# replace your_email and your password with your original emailid and password 
    server.sendmail('your_mail','to','content')# and here replace your_mail with your original mailid
    server.close()

if __name__=="__main__":
    wish()
    print("i am a good boy")
    speak("i am a good boy")

    #while 1:
    while 1:
        query=take().lower()  #taking voice query

        if 'wikipedia' in query:
            speak('searching wikipedia')
            query=query.replace("wikipedia","") 
            results=wikipedia.summary(query,sentences=2)
            speak("Acording to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
            
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

        elif 'time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak("sir, now the time is "+strTime)

        elif 'open code' in query:
            codepath="E:\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)

        elif 'send mail' in query:
            try:
                speak("what should i say")
                content=take()#message to the contact
                to=#take()#"toaddress"# here you can keep to address directly or you can take from voice by take() method
                sendEmail(to,content)
                speak("email has been sent")
            except Exception as e:
                print('e')
                speak("sorry sir, i am not able to send the email ")
