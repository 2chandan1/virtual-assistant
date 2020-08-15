import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices= engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice',voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour= int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning !")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("hello ,sir . i am ciri . how are you .")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listining....")
        r.pause_threshold=1
        audio=r.listen(source)
    
    try:
        print("Recognizing...")
        query= r.recognize_google(audio,language='en-in')
        print(f"User said:{query}\n")
    except Exception as e:
        print(e)

        print("say that again pleas...")
        return "None"
    return query    

def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('tiwarichandan936@gmail.com','Chandan@1234')
    server.sendmail('tiwarichandan936@gmail.com',to,content)
    server.close()



if __name__ == "__main__":
    #speak("chandan is a boy")
    wishMe()
    while True:
        query=takeCommand().lower()

    # Logic for executing tasks based query
        if 'wikipedia' in query:
            speak('Searching wikipedia..')
            query=query.replace("Wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        
        elif 'how are you' in query:
            speak("i am also good. what can i do for you ?")
        
        elif 'open youtube' in query:
            webbrowser.open("https://www.youtube.com/")

        elif 'open google' in query:
            webbrowser.open("https://www.google.com")
        
        elif 'open gmail' in query:
            webbrowser.open("https://www.gmail.com")

        elif 'open ims' in query:
            webbrowser.open("https://uims.cuchd.in/UIMS/Login.aspx")

        elif 'open bb' in query:
            webbrowser.open("https://cuchd.blackboard.com/?new_loc=%2Fultra%2Fstream")

        elif 'open facebook' in query:
            webbrowser.open("www.facebook.com")


        elif 'play music' in query:
            music_dir="C:\\Users\\chandan\\Music\\Favorit songs2"
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[1]))

        elif 'the time'in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir, the time is{strTime}")
        elif 'open code' in query:
            codepath="C:\\Users\\chandan\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)

        
        elif 'email to chandan' in query:
            try:
                speak("what should i say?")
                content=takeCommand()
                to="tiwarianmol870@gmail.com"
                sendEmail(to,content)
                speak("email sent..!")
            except Exception as e:
                print(e)
                speak("email not sent!")

        elif 'stop' in query:
            speak("thank you for your time")
            exit()

        
        
      