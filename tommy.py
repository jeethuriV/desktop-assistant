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
    
def wish():
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

def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    emailaddress=take()
    server.login(emailaddress,'123456789@J1')
    server.sendmail(emailaddress,'to','content')
    server.close()

if __name__=="__main__":
    wish()
    print("i am a good boy")
    speak("i am a good boy")

    #while 1:
    if 1:
        query=take().lower()

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
            music_dir= 'D:\\MY MUSIC\\Aarya 2'
            songs=os.listdir(music_dir)
            print(songs)
            j=random.randint(0,len(songs)-1)
            os.startfile(os.path.join(music_dir,songs[j]))

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
                content=take()
                to='jeethurivishnu@gmail.com'#take()
                sendEmail(to,content)
                speak("email has been sent")
            except Exception as e:
                print('e')
                speak("sorry sir, i am not able to send the email ")
