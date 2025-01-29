
### **Orion: Voice-Activated Assistant** 
Orion is a voice-activated personal assistant designed to make your tasks easier and faster. It can respond to your commands, provide the current date and time, open popular websites, and even play music. The project is written in Python and uses several libraries to enable speech recognition, text-to-speech, and browser control.

## **Features**
- Voice Commands: Activate Orion by saying "Orion" and give it a command.
- Text-to-Speech: Orion talks back to you with helpful responses.
- Open Websites: Quickly access Google, Facebook, LinkedIn, and more.
- Date and Time: Ask Orion for the current date or time.
- Music Playback: Play songs from a predefined library.
- Custom Responses: Orion will politely let you know if it doesn't understand a command.

## **Technologies Used**
Python: Programming language used for the entire project.
SpeechRecognition: For recognizing voice commands from the microphone.
Pyttsx3: For converting text to speech.
Webbrowser: To open websites directly in your browser.
Datetime: To fetch the current date and time.

## **For setting up the project**
1. 1.1 created a virtual environment using "python -m venv venv1" on terminal
   1.2 "Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass -Force" on console before 1.1 if scripts were disabled
   1.3 run ".\venv1\Scripts\Activate.ps1" on command line
   1.4 virtual env created
2. installed the following using pip:
    2.1 speechrecognition 
    2.2 pyaudio
    2.3 setuptools
    2.4 pyttsx3
    2.5 openai
3. run the file using "venv1\Scripts\python.exe main.py" on terminal
