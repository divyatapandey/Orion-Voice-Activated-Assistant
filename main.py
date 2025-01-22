# main.py
import speech_recognition as sr
import webbrowser
import pyttsx3
from datetime import datetime
import musiclibrary

#initialsing the engine
engine= pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    if "date" in c.lower():
        now = datetime.now()
        date = now.strftime("%Y-%m-%d")
        speak(date)
    elif "time" in c.lower():
        now = datetime.now()
        time = now.strftime("%H:%M:%S")
        speak(time)
    elif "open google" in c.lower():
        speak("ok")
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        speak("ok")
        webbrowser.open("https://facebook.com")
    elif "open linkedin" in c.lower():
        speak("ok")
        webbrowser.open("https://linkedin.com")
    elif c.lower().startswith("play"):
        song=c.lower().split(" ")[1]
        link=musiclibrary.music[song]
        webbrowser.open(link)
    elif "bye" in c.lower():
        speak("bye! See you later")
        exit()
    else:
        speak("Thankyou, I am still learning. I will learn this command too")
        #let open ai handle the request

if __name__=="__main__":
    speak("Initialising Orion...")
    while True:
        #listen for the wake word orion
        #obtain audio from the microphone
        # Reading Microphone as source
        # listening the speech and store in audio_text variable
        #creating a recogniser object # Initialize recognizer class (for recognizing the speech)
        r=sr.Recognizer()
            # recoginze_() method will throw a request
            # error if the API is unreachable,
            # hence using exception handling
            
        try:
            with sr.Microphone() as source:
                print("Listening..")
                audio= r.listen(source,timeout=2,phrase_time_limit=1)
                # using google speech recognition
            word=r.recognize_google(audio)
            if(word.lower()=="orion"):
                #listen for command
                with sr.Microphone() as source:
                    speak("Yes")
                    print("Orion activated..")
                    audio= r.listen(source)
                    command=r.recognize_google(audio)

                    processCommand(command)
        except Exception as e:
            print("Sorry, I did not get that")