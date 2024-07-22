import datetime
import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

print("This is your voice assistant \n _____  _      __       __     _    ___\n|  _  |(_) _ _ \\ \\  _  / /___ | |  |  _|\n| |_| || || '_| \\ \\/ \\/ // _ \\| |_ | |_ \n|_| |_||_||_|    \\_/ \\_/ \\___/|___||_| \tspeaking...."); 

engine = pyttsx3.init('sapi5') #through which windows give an api to take voice
voices = engine.getProperty('voices')
#voices[0].id = david (male) voices[1].id = zira (female)
engine.setProperty('voice', voices[0].id)

def say(audio):
    print(audio)
    engine.say(audio)
    engine.runAndWait()

def greet():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        say("Good Morning! I hope you have a great start to the day.")
    elif hour >= 12 and hour < 18:
        say("Good Afternoon!")
    else:
        say("Good Evening!")
    say("This is AirWolf speaking. Is there any way i may be of use to you?")

def listen(): # microphone input from user and returns string ouput
    r = sr.Recognizer() #Recognizer is the class having attributes such as pause_threshold etc. r would be the instance
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1 #to ensure the query isnt completed when user is just taking a pause (limit of 1 second)
        r.adjust_for_ambient_noise(source, duration=1) #to adjust for any background noise.
        voice = r.listen(source)
        print("Audio captured")
    try:
        query = r.recognize_google(voice, language = 'en-US') #google web speech AI
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again please...")
        return "None"    
    return query

if __name__ == "__main__":
    greet()
    while True:
        query = listen().lower()

        if 'wikipedia' in query:
            say("Searching from Wikipedia....")
            query = query.replace("wikipedia", "")
            search = wikipedia.summary(query, sentences = 2)
            say("According to Wikipedia")
            print(search)
            say(search)

        elif 'open facebook' in query:
            webbrowser.open("facebook.com")
        elif 'open linkedin' in query:
            webbrowser.open("linkedin.com")
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'the time' in query:
            stringTime = datetime.datetime.now().strftime("%H:%M:%S")
            say(f"Currently the time is {stringTime}")

        elif 'a way out' in query:
            path = "C:\Games\A Way Out\Haze1\Binaries\Win64\AWayOut.exe"
            os.startfile(path)

        elif 'write an email' in query:
            try:
                say("What do you want to write?")
                content = listen()
                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.ehlo()
                server.starttls()
                server.login('ur-email', 'ur-password')
                server.sendmail('ur-email', 'sender-email', content)
                #u have to write the email credentials u want to send from in line 85 and sender's email in line 86
                server.close()
                say("Email has been sent")
            except Exception as e:
                say("Sorry your email was not sent")
          