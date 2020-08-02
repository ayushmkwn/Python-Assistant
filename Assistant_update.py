# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 15:55:25 2020

@author: 107,092,122
"""
#Internet Connection is required for run this program smoothly

import pyttsx3                            
import speech_recognition as sr
from time import ctime
import datetime 
import wikipedia
import os
import pythoncom
import webbrowser
import random
import smtplib
import wolframalpha 
from selenium import webdriver
import re

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices)
print(voices[0].id)
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning BOSS!!")
        print("Good Morning BOSS!!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon BOSS!!")
        print("Good Afternoon BOSS!!")
    else:
        speak("Good Evening BOSS!!")
        print("Good Evening BOSS!!")
    speak("I am your assistant. How can i help you BOSS")
    print("I am your assistant. How can i help you BOSS")


def takeCommand():
    ''' take microphone input from user nd return string o/p'''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        #print(e)
        print("I don't recognize...")
        return "None"
    return query

#func() for sending mail
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('name.is.ash.12@gmail.com','A@sh908070')
    server.sendmail('name.is.ash.12@gmail.com',to,content)
    server.close()


def search_web(query):
    #for YouTube search
    if 'youtube' in query:
        speak("what do you want to search")
        qry = takeCommand().lower()
        speak("Searching in YouTube")
        webbrowser.open(f"https://www.youtube.com/results?search_query={qry}") 
        return
    #for Google search
    if 'google' in query: 
        speak("what do you want to search")
        qry = takeCommand().lower()
        speak("Searching in Google Chrome")
        webbrowser.open(f"https://www.google.com/search?q={qry}") 
    return


def opencmd(query):
    #open gmail in your default browser
    if 'gmail' in query:
        speak("Sure")
        speak("opening Gmail")
        webbrowser.open("https://mail.google.com/mail/u/1/#inbox")

    #open YouTube in your default browser
    elif 'youtube' in query:
        speak("sure")
        speak("opening youtube")
        webbrowser.open("https://www.youtube.com/")
    
    #open Visual Studio Code in your Computer
    elif 'code' in query:
        speak("Sure")
        speak("opening microsoft visual code")
        codepath = "C:\\Users\\ayush\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(codepath)

    #open Chrome in your Computer
    elif 'chrome' in query:
        speak("Sure")
        speak("opening chrome")
        cp = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
        os.startfile(cp)

    #open Dec C++ in your Computer
    elif 'dev c plus plus' in query:
        speak("Sure")
        speak("opening dev c plus plus")
        cp = "C:\\Program Files (x86)\\Dev-Cpp\\devcpp.exe"
        os.startfile(cp)
    return


if __name__ == "__main__":
    wishMe()
    #while True:
    query = takeCommand().lower()
    #logic
    #for wikipedia search
    if 'wikipedia' in query:
        speak("Searching wikipedia...")
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        speak("According to wikipedia")
        speak(results)
    
    #for coronavirus traking
    elif 'coronavirus tracker' in query:
        webbrowser.open("https://www.covid19india.org/")
    
    elif 'who are you' in query:
        speak("I am Assistant created by 3 students")

    #for play a small game
    elif 'play game' in query:
        speak("Awwwwww Let's play dude")
        speak("which one is bigger 1.20 or 1.2 ?")
        query=takeCommand().lower()
        if 'one point two' in query:
            speak("Ohh yeah you are not math student hahahaha")
        if 'one point twenty' in query:
            speak("Ohh yeah you are not math student hahahaha")
        if 'both are same' in query:
            speak("Well doneee baabalu, yor are topper ammmmmmmmmmmm from last haa-aa haa , don't take seriously baabalu.")
        else:
            speak("kya yaaarr sahi se bol naa")

    #search for any of the content in Google or YouTube
    elif 'search' in query:
        search_web(query)

    #play random movie from computer
    #path may have specified so run on other computer change path in 'movie_dir'
    elif 'play movie' in query:
        speak("Okay")
        speak("play movie from your computer")
        movie_dir = 'D:\\3_Movies'
        movies = os.listdir(movie_dir)
        n=random.randrange(5,29,2)
        os.startfile(os.path.join(movie_dir,movies[n]))
    
    #give a current time
    elif 'the time' in query:
        speak("Sure")
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"Sir, the time is {strTime}")
        print(strTime)
    
    #open some of apps in computer
    #like speak 'open code' for Visual Studio Code
    #may path is specified so you can change it in opencmd function
    elif 'open' in query:
        opencmd(query)

    #for send mail to other person
    # receiver email & sender email has specified you can change it from sendEmail() function    
    elif 'send email' in query:
        try:
            speak("what do you want to send?")
            content = takeCommand()
            to = "18bce092@nirmauni.ac.in"
            sendEmail(to, content)
            speak("Email has been sent")
            print("Email has been sent")
        except Exception as e:
            print(e)

    else:
        speak("Sorry i didn't get it please say again")
