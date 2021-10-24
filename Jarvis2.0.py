import asyncio
import configparser
import datetime
import glob
import json
import operator
import os
import re
import smtplib
import socket
import subprocess
import sys
import time
import tkinter.filedialog as filedialog
import urllib.request
import webbrowser
from multiprocessing import freeze_support
from os import startfile
from time import localtime, strftime
from tkinter import *

import geocoder
import geopy
import googletrans
import gtts
import instaloader
import keyboard
import kivy
import meaning
import my_package
import playsound
import psutil
import pyautogui
import PyDictionary as Diction
import pygame
import pyjokes
import PyPDF2
import python_weather
import pyttsx3
import pywhatkit
import pywikihow
import qrscan
import requests
import speech_recognition as sr
import speedtest
import synonym
import twilio
import wikipedia
import wolframalpha
from bs4 import BeautifulSoup
from geopy.distance import great_circle
from geopy.geocoders import nominatim
from googletrans import Translator
from keyboard import press, write
from kivy.app import App
from playsound import playsound
from pyautogui import click
from pygame import mixer_music
from requests.api import request
from wikipedia.wikipedia import USER_AGENT

kivy.require('1.9.0') 
from kivy.animation import Animation
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.properties import NumericProperty, StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

doss = os.getcwd()

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
engine.setProperty('rate',180)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def sendEmail(to, content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login('shanmugamganesan59@gmail.com', 'amutha54321')
    server.sendmail('shanmugamganesan59@gmail.com', to, content)
    server.close()

def YouTubeAuto():
    speak("what is your command?")
    print("what's your command?")
    comm = takecommand()

    if 'pause' in comm:
        keyboard.press('space bar')
    elif 'restart' in comm:
        keyboard.press('0')
    elif 'mute' in comm:
        keyboard.press('m')
    elif 'skip' in comm:
        keyboard.press('l')
    elif 'back' in comm:
        keyboard.press('j')
    elif 'full screen' in comm:
        keyboard.press('f')
    elif 'film mode' in comm:
        keyboard.press('t')
    speak("done sir")

async def getweather():
    # declare the client. format defaults to metric system (celcius, km/h, etc.)
    client = python_weather.Client(format=python_weather.IMPERIAL)

    # fetch a weather forecast from a city
    weather = await client.find("Chennai")

    # returns the current day's forecast temperature (int)
    print(weather.current.temperature)

    # get the weather forecast for a few days
    for forecast in weather.forecasts:
        print(str(forecast.date), forecast.sky_text, forecast.temperature)

    # close the wrapper once done
    await client.close()

def Wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("welcome back sir")
    elif hour>=12 and hour<18:
        speak("good afternoon sir")
    else:
        speak("good evening sir")
    speak("Loading JARVIS")
    speak("lOADING MODULES")
    speak("rendering main control services")
    speak("loading custom user profiles")
    speak("getting ready")
    speak("loading intro")
    intro_dir = 'C:\\Users\\SHANMUGAM\\Videos\\JARVIS Intro'
    intro = os.listdir(intro_dir)
    os.startfile(os.path.join(intro_dir, intro[0]))
    time.sleep(13)
    os.system("TASKKILL /F /IM vlc.exe")
    speak("I am online and ready")
    speak("JARVIS at your service, please tell me how may i help you")

def Dict():
    speak("activated dictionary")
    print("Activated Dictionary")
    speak("tell me the problem,sir")
    prob1 = takecommand()

    if 'meaning' in prob1:
        prob1 = prob1.replace("what is the","")
        prob1 = prob1.replace("jarvis","")
        prob1 = prob1.replace("of","")
        prob1 = prob1.replace("meaning of","")
        result = Diction.meaning(prob1)
        speak("the meaning for {prob1} is {result}")
    elif 'synonym' in prob1:
        prob1 = prob1.replace("what is the","")
        prob1 = prob1.replace("jarvis","")
        prob1 = prob1.replace("of","")
        prob1 = prob1.replace("synonym of","")
        result = Diction.synonym(prob1)
        speak("the synonym for {prob1} is {result}")
    elif 'antonym' in prob1:
        prob1 = prob1.replace("what is the","")
        prob1 = prob1.replace("jarvis","")
        prob1 = prob1.replace("of","")
        prob1 = prob1.replace("antonym of","")
        result = Diction.antonym(prob1)
        speak("the antonym for {prob1} is {result}")
    speak("Exited Dictionary")
    print("EXITED DICTIONARY!")

def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        r.energy_threshold = 3000
        audio = r.listen(source)
    try:
        print("Recogonizing...")
        print("wait for few Moments")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said:{query}\n")

    except Exception as e:
        print(e)
        speak("boss i request you to say that again")
        return "none"
    return query

if __name__ =="__main__":
    Wishme()
    takecommand()
    freeze_support()
    while True:
        query=takecommand().lower()  
        if "wikipedia" in query:
            speak("searching in wikipedia")
            query=query.replace("wikipedia","") 
            results=wikipedia.summary(query,sentences=3)
            speak("According to wikipedia")
            print (results)
            speak("got it!")
            speak(results)
        elif 'take a note' in query:
            speak("what should I write?")
            note_text = takecommand()
            if(note_text!=None):
                 f = open('notes.txt','a')
                 timestamp = datetime.datetime.now().strftime("%H:%M:%S")
                 f.write(timestamp + '\n')
                 note = note_text + '\n\n'
                 f.write(note)
                 f.close()
        elif 'can you calculate' in query:
            r = sr.Recognizer()
            with sr.Microphone() as source:
                speak("say me, what do you want to calculate , sir")
                print('listening....')
                r.adjust_for_ambient_noise(source)
                audio = r.listen(source)
            my_string = r.recognize_google(audio)
            print(my_string)
            def get_operator_fn(op):
                return{
                    '+' : operator.add,
                    '-' : operator.sub,
                    'x' : operator.mul,
                    'divided' : operator.__truediv__,
                }[op]
            def eval_binary_expr(op1, oper, op2):
                op1,op2 = int(op1), int(op2)
                return get_operator_fn(oper)(op1, op2)
            speak("your result is..")
            speak(eval_binary_expr(*(my_string.split())))
        elif'open youtube' in query:
           webbrowser.open("youtube.com")
           speak("opening youtube boss") 
        elif 'open google'   in query:
           webbrowser.open("google.com") 
           speak("opening google boss")
        elif 'youtube search' in query:
            speak("ok sir. this is what I found for your search")
            query = query.replace("jarvis","")
            query = query.replace("youtube search","")
            web = 'https://www.youtube.com/results?search_query=' + query
            webbrowser.open(web)
            speak("done sir")
        elif 'pause' in query:
            keyboard.press('space bar')
        elif 'restart' in query:
            keyboard.press('0')
        elif 'mute' in query:
            keyboard.press('m')
        elif 'skip' in query:
            keyboard.press('l')
        elif 'back' in query:
            keyboard.press('j')
        elif 'full screen' in query:
            keyboard.press('f')
        elif 'film mode' in query:
            keyboard.press('t')
        elif 'youtube automation' in query:
            YouTubeAuto()
        elif 'google search' in query:
            speak("ok sir. this is what I found for your search")
            query = query.replace("jarvis","")
            query = query.replace("google search","")
            pywhatkit.search(query)
            speak("done sir")
        elif 'website' in query:
            speak("ok sir. Launching....")
            print("ok Sir. Launching....")
            query = query.replace("jarvis","")
            query = query.replace("website","")
            web1 = query.replace("open","")
            web2 = 'https://www.' + web1 + '.com'
            webbrowser.open(web2)
            speak("launched")
        elif 'launch' in query:
            speak("tell me the name of the website, sir")
            print("tell me the name of the website,sir")
            name = takecommand()
            web = 'https://www.' + name + '.com'
            webbrowser.open(web)
            speak("launching website")
            print("launching website...")
        elif 'play music' in query:
            music_dir = 'D:\Music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
        elif 'pause music' in query:
            pyautogui.press('spacebar')
        elif 'whatsapp message' in query:
            speak("what message should I send , sir?")
            print("what message should I send , sir?")
            q1=takecommand()
            pywhatkit.sendwhatmsg("+917010535407",q1,1,5)
        elif 'logout' in query:
            os.system("shutdown -1")
        elif 'restart' in query:
            os.system("shutdown /r /t 1")
        elif 'shutdown' in query:
            pywhatkit.shutdown(time=60)
            speak("your system will shutdown in 60 seconds")
        elif 'cancel shutdown' in query:
            pywhatkit.cancel_shutdown()
            speak("you cancelled your scheduled shutdown protocol ,sir")
            print("you cancelled your scheduled shutdown protocol ,sir")
        elif 'resume music' in query:
            pyautogui.press('spacebar')
        elif 'next music' in query:
            pyautogui.press('n')           
        elif 'previous music' in query:
            pyautogui.press('p')
        elif 'stop music' in query:
            os.system("TASKKILL /F /IM vlc.exe")
        elif 'who is your creator' in query:
            print("My creator's name is SHANMUGAM")
            speak("My creator's name is SHANMUGAM")
        elif 'repeat my words' in query:
            speak("speak sir")
            jj = takecommand()
            speak(f"you said:{jj}")
        elif 'check instagram profile' in query:
            speak("please enter the username correctly,sir")
            print("please enter the username correctly,sir")
            name = input("Enter your username here:")
            webbrowser.open(f'www.instagram.com/{name}')
            speak(f'sir this is the profile of the user you entered {name}')
            time.sleep(5)
            speak("would you like to download the profile picture of this account, sir")
            condition = takecommand().lower()
            if 'yes' in condition:
                mod = instaloader.Instaloader()
                mod.download_profile(name, profile_pic_only=True)
                speak("I am done sir. The profile picture is saved in our main folder. Now I am ready for your next command , sir")
                print("I am done sir. The profile picture is saved in our main folder. Now I am ready for your next command , sir")
            else:
                pass
        elif'take screenshot' in query:
            speak("sir, please tell me the name for this screenshot")
            print("sir, please tell me the name for this screenshot")
            name = takecommand().lower()
            speak("sir, please hold the screen for few seconds , I am taking a screenshot")
            print("sir, please hold the screen for few seconds , I am taking a screenshot")
            time.sleep(3)
            img = pyautogui.screenshot()
            img.save(f"{name}.png")
            speak("I am done sir. The screenshot is saved in our main folder. I am ready for your next command sir")
            print("I am done sir. The screenshot is saved in our main folder. I am ready for your next command sir")        
        elif "internet speed" in query:
            try:
                os.system('cmd /k "ping google.com"')
            except:
                speak("there is no internet connection")
        elif "send message" in query:
            speak("what should I send sir")
            print("what should I send sir")
            msz = takecommand()
            from twilio.rest import Client 
            account_sid = 'ACc552324313d738741852e660d455f88d'
            auth_token = 'b1933c42896857bf18dba66579441fef'
            client = Client(account_sid, auth_token)
            message = client.messages \
                .create(
                    body= msz,
                    from_='+12184058268',
                    to='+917010535407'
                )
            print(message.sid)
            speak("message has been sent successfully")
            print("message has been sent successfully")
        elif 'volume up' in query:
            pyautogui.press("volumeup")
        elif 'volume down' in query:
            pyautogui.press("volumedown")
        elif 'mute' in query:
            pyautogui.press("mute")
        elif 'play movie' in query:
            movie_dir = 'Videos'
            videos = os.listdir(movie_dir)
            print(videos)
            os.startfile(os.path.join(movie_dir, videos[0]))
        elif 'pause movie' in query:
            pyautogui.press('spacebar')
        elif 'resume movie' in query:
            pyautogui.press('spacebar')
        elif 'next movie' in query:
            pyautogui.press('n')
        elif 'previous movie' in query:
            pyautogui.press('p')
        elif 'stop movie' in query:
           os.system("TASKKILL /F /IM vlc.exe") 
        elif 'open calculator' in query:
            subprocess.Popen(['C:\\Windows\\System32\\calc.exe'])
            speak("opening calculator boss")
        elif 'open control panel' in query:
            subprocess.Popen("control.exe")
        elif 'open notepad' in query:
            subprocess.Popen(['C:\\Windows\\System32\\notepad.exe'])
            speak("opening notepad boss")
        elif 'open wordpad' in query:
            subprocess.Popen(['C:\\Windows\\System32\\write.exe'])
            speak("opening wordpad boss")
        elif 'open paint' in query:
            subprocess.Popen(['mspaint.exe'])
            speak("opening microsoft paint boss")
        elif 'open cmd' in query:
            subprocess.Popen(['cmd.exe'])
            speak("opening command process boss")
        elif 'type' in query:
            query = query.replace("type","")
            pyautogui.typewrite(f"{query}",0.1)
        elif 'locate me' in query:
            speak("tracking you down sir")
            print("tracking you down sir")
            YOUR_GEOLOCATION_KEY = '5e70348d82344b87bb0686df045875e5'

                # IP address to test
            ip_address = '2409:4072:588:378e:1023:d5c7:7df0:57b2'

            content = urllib.request.urlopen('https://ipgeolocation.abstractapi.com/v1/?api_key=' + YOUR_GEOLOCATION_KEY + '&ip_address=' + ip_address)
            read_content = content.read()
            speak("found you sir")
            print(read_content) 
        elif 'open powershell' in query:
            subprocess.Popen(['powershell.exe'])
            speak("opening powershell boss")
        elif 'tell me news for today' in query:
            speak("News for today")
            url = "https://newsapi.org/v2/top-headlines?country=in&apiKey=3f52edc3c9a945e58348656f101fa866"
            news = requests.get(url).text
            news_json = json.loads(news)
            print(news_json["articles"])
            arts = news_json['articles']
            for articles in arts:
                speak(articles['title'])
                speak("Moving to the next news...listen carefully")

            speak("Thanks for listening...")
        elif 'say what the time is' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"SIR,The time is {strTime}")
        elif 'say some jokes' in query:
            speak("saying jokes , sir")
            speak(pyjokes.get_joke())
        elif 'thank you' in query:
            speak("you are welcome sir")
            print("you are welcome, sir")
        elif 'weather' in query:
            speak("which city?")
            city = takecommand()
            apiKey = 'd97c5f1113dc0326d9c0abbfa25f0227'
            response = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={apiKey}&units=metric')
            x = response.json()
            if x["cod"] != "404":
                y = x['main']
                temperature = x['main']["temp"]
                pressure = x['main']["pressure"]
                humidity = x['main']["humidity"]
                desc = x["weather"][0]["description"]
                weather_detail = f'Current temperature is {temperature}, pressure is {pressure} hPa, humidity is {humidity} %, Weather condition is {desc}'
                speak(weather_detail)
                print(weather_detail)
                
            
            else:
                speak('Sorry, could not find the city')  
        elif 'get forecast' in query:
            speak("getting forecasts")
            loop = asyncio.get_event_loop()
            loop.run_until_complete(getweather())
        elif "what is your name" in query:
            speak("Sir I am Jarvis.just a rather very intelligent system and I am your personal assistant ")
        elif 'open stackoverflow' in query:
            webbrowser.open('https://stackoverflow.com/')
        elif 'open code' in query:
            codePath = "C:\\Users\\SHANMUGAM\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        elif "open chrome" in query:
            speak("opening chrome boss")
            codepath1="C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"
            os.startfile(codepath1)
        elif "activate how to do mod" in query:
            from pywikihow import search_wikihow
            speak("how to do mod activated successfully boss say what you want to know")
            how = takecommand()
            max_results = 1
            how_to = search_wikihow(how, max_results)
            assert  len(how_to) == 1
            how_to[0].print()
            speak(how_to[0].summary)
        elif 'activate dictionary' in query:
            Dict()
        elif 'alarm' in query:
            speak("Enter the time sir")
            time = input(": Enter The Time :")

            while True:
                Time_Ac =datetime.datetime.now()
                now = Time_Ac.strftime("%H:%M:%S")

                if now == time:
                    speak("Time to wake up sir")
                    playsound("beep.mp3")
                    speak("alarm closed")
        elif 'check system resources' in query:
            print('The CPU usage is: ', psutil.cpu_percent(4))
            print('RAM memory % used:', psutil.virtual_memory()[2])
        elif 'send email' in query:
            try:
                speak("What should I say boss?")
                content = takecommand()
                to = "shanmugamganesan59@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent successfully boss")
            except Exception as e:
                print(e)
                speak("Sorry boss I am not able to send this email")  
        elif "bye" in query:
            speak("initializing shutdown protocol")
            speak("good bye sir")
            print("good bye ,sir")
            exit()
      