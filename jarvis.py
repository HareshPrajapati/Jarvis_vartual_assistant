import pyttsx3
import speech_recognition as sr
import wikipedia
import datetime
import urllib3
# import webbrowser
import os
import re
import smtplib



import speech_recognition as sr
import os
import sys
import re
import webbrowser 
import smtplib
import requests
import subprocess
from pyowm import OWM
import youtube_dl
import vlc
import urllib
import urllib3
import json
from bs4 import BeautifulSoup, BeautifulSoup
# from urllib3 import urlopen
import wikipedia
import random
from time import strftime
import urllib.request






engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def jarvinResponse(audio):
    # "speaks audio passed as argument"
    print(audio)
    for line in audio.splitlines():
        os.system(audio)

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Harry!")
    elif hour >= 12 and hour < 18:
        speak("Good AfterNoon Harry!")
    else:
        speak("Good Evening Harry!")
    speak("I M MikroTroniks. How May I help You")


def TakeCommand():
    '''


    it take microphone input from user and return as a string


    '''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said :  {query}\n")

    except Exception as e:
        print(e)
        speak("Say That Again Please....")
        return "None"

    return query

def process_text(input):
    try:
        if 'the time' in input:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir , the time is {strTime}")


        if 'open visual' in input:
            codepath = "C:\\Users\\Haesh_MikoToniks\\AppData\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)
            speak("visual studio has been open")


        if 'open opera' in input:
            codepath = "C:\\Users\\Haesh_MikoToniks\\AppData\\Local\\Programs\\Opera\\opera.exe"
            os.startfile(codepath)
            speak("opera browser has been open")


        if 'open skype' in input:
            codepath = "C:\\Program Files (x86)\\Microsoft\\Skype for Desktop\\Skype.exe"
            os.startfile(codepath)
            speak("skype has been open")


        if 'open mp lab' in input or 'open MPL app' in input:
            codepath4 = "C:\\Program Files (x86)\\Microchip\MPLABX\\v5.20\\mplab_platform\\bin\\mplab_ide64.exe"
            os.startfile(codepath4)
            speak("mplab has been open")


        if 'open chrome' in input:
            codepath5 = "C:\\Chrone\\chrome.exe"
            os.startfile(codepath5)
            speak("chrome browser has been open ")

        if 'open mikrosoft' in input:
            codepath5 = "C:\\Program Files (x86)\\Microsoft\Edge\\Application\\msedge.exe"
            os.startfile(codepath5)
            speak("mikrosoft edge has been open")
        
        if 'open driver' in input:
            codepath5 = "C:\\Program Files (x86)\\IObit\\Driver Booster\\7.5.0\\DriverBooster.exe"
            os.startfile(codepath5)
            speak("driver booster has been open")
        
        if 'open code blocks' in input:
            codepath5 = "C:\\Program Files\\CodeBlocks\\codeblocks.exe"
            os.startfile(codepath5)
            speak("codeblocks has been open")

        if 'open vlc' in input:
            codepath5 = "C:\\Program Files (x86)\\VideoLAN\VLC\\vlc.exe"
            os.startfile(codepath5)
            speak("vlc media player has been open")

        if 'open ardu' in input:
            codepath5 = "C:\\Program Files (x86)\\Arduino\\arduino.exe"
            os.startfile(codepath5)
            speak("arduino has been open")


        if 'open notepad' in input:
            codepath5 = "C:\\Program Files (x86)\\Notepad++\\notepad++.exe"
            os.startfile(codepath5)
            speak("notepad has been open")


        if 'open logic' in input:
            codepath5 = "C:\\Program Files\\Saleae Inc\\Logic.exe"
            os.startfile(codepath5)
            speak("logic analizer has been open")

        if 'open real' in input:
            codepath5 = "C:\\Program Files (x86)\\BEL\\Realterm\\realterm.exe"
            os.startfile(codepath5)
            speak("real term has been open")


        if 'open file' in input:
            codepath5 = "C:\Program Files\File Magic\FileMagic.exe"
            os.startfile(codepath5)
            speak("filemagic has been open")


        if 'open an installer' in input or 'open un installer' in input or 'open installer' in input:
            codepath5 = "C:\\Program Files (x86)\\IObit\\IObit Uninstaller\\IObitUninstaler.exe"
            os.startfile(codepath5)
            speak("iobitunistaller has been open")


        if 'open Ip' in input:
            codepath5 = "C:\\Users\\Haesh_MikoToniks\\AppData\\Local\\IPMsg\\IPMsg.exe"
            os.startfile(codepath5)
            speak("ip massenger has been open")


        if 'open pycharm' in input:
            codepath5 = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2020.1.2\\bin\pycharm64.exe"
            os.startfile(codepath5)
            speak("paycharm has been open")
          
        if 'search' in input:
            speak('what should i search')
            opera_path = 'C:/Users/Haesh_MikoToniks/AppData/Local/Programs/Opera/opera.exe %s'
            browser_path = 'C:/Program Files/Internet Explorer/iexplore.exe %s'
            chrome_path = 'C:/Chrone/chrome.exe %s'
            r = sr.Recognizer()
            with sr.Microphone() as source:
                print('say something..')
                audio = r.listen(source)
                print('Done')
            try:
                text =  r.recognize_google(audio)
                print('google think you said:\n' +text)
                webbrowser.get(browser_path).open(text)
                speak(f" your search {text} has been open in defoult browser")
                
                
            except Exception as e:
                print(e)

       
    except Exception as e:
           print(e)






if __name__ == "__main__":
    wishMe()
    while True:
        query = TakeCommand().lower()
        process_text(query)

        if 'go offline' in query:
            speak("ok sir ! shutting down the system and exiting")
            quit()


 