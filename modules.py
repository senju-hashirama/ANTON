#modules.py

#install all these modules, they are easy to install but you will face problem while installing pyaudio
#do not panic or give up. You will find many videos on youtube on how to install it so follow those and install pyaudio.

import pyttsx3 #text to speech module

import speech_recognition as sr 

import winsound

from wakeonlan import send_magic_packet

import subprocess

import wikipedia

import pyautogui #controls keyboard and mouse movement and detects icons.

import os

from bs4 import BeautifulSoup

import requests

import time

import random

from plyer import notification
#functions

def speak(text):#uses pyttsx3 and sapi5 engine to convert text to speech
    engine=pyttsx3.init("sapi5")#change this if on other os other than windows

    engine.setProperty('rate',170)
    
    engine.setProperty('volume', '1')
    
    engine.say(text)
   
    
    engine.runAndWait()
 
def listen():#requires internet connection.
    
    r=sr.Recognizer()
    sr.Recognizer.dynamic_energy_threshold = False


    r.energy_threshold = 430  
    
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)

        try:      
            audio=r.listen(source,timeout=1.5)     
            
            txt=(r.recognize_google(audio))

            if txt !=None:#returns the text spoken.
                winsound.Beep(2000,100)
                return txt
        except:

            return None         #returns none if nothing is spoken or when there is some error.
         
def wakeup(mac):#turns on a device connected to the same network if wake on lan is enabled on the device.
    #this also requires external wifi adapter with packet injection.you can use this function on a mobile using pydroid.

    for i in range(5):

                send_magic_packet(mac)

def facts():
    r=requests.get("https://www.thefactsite.com/1000-interesting-facts/{}/" .format(random.randint(1,10)))
    soup=BeautifulSoup(r.content,features="lxml")
    d=soup.find_all("p",class_="list")
    maxl=len(d)
    txt=d[random.randint(0,maxl)]
    sdata=txt.text
    notification.notify(
            title="A.N.T.O.N",
            message=sdata,
            timeout=10)
    speak(sdata)
    
    
def google(search): #opens chrome and displays the search result  
    data1=search.split(" ")
    str1=""
    for i in data1:
                str1=str1+i+"+"
    b="start chrome https://www.google.com/search?q="+str1
    #the search item is seperated by "+" and concatinated here .THen the subprocess module is used to open cmd and launch chrome 
    
    out=subprocess.run(b,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True)
    
   

def browser(search): #if the pc does not have chrome use this.Google search opens on some browser Eg:on windows 10 it opens in opera
    data1=search.split(" ")
    str1=""
    for i in data1:
                str1=str1+i+"+"

    b="start https://www.google.com/search?q="+str1
    out=subprocess.run(b,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True)
    
 


def wiki(search): #gives a summary  of the text passed .The number of lines can be changed in line 82 

    try:
        if search!=None:
                print(search)    
                data=str(wikipedia.summary(search,sentences=2))
                print(data)
                speak(data)
    except:
        speak("i could not search for "+search)

def youtube(search):#opens chrome and reutrns the search results
            data1=search.split(" ")
            str1=""
            for i in data1:
                str1=str1+i+"+"
            b="start chrome https://www.youtube.com/results?search_query="+str1
            out=subprocess.run(b,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True)

def stack(search):#opens stackoverflow and reurns the result
            data1=search.split(" ")
            str1=""
            for i in data1:
                str1=str1+i+"+"
            speak("opening stackoverflow")

            b="start chrome https://stackoverflow.com/search?q="+str1
            out=subprocess.run(b,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True)


def screenshot():#takes screenshot and saves it in the current dir where the file is present.
                 #say capture to take the scrrenshot
    speak("ready when you are")
    txt=listen()
    if txt.lower()=="capture":
                        im1 = pyautogui.screenshot()
                        im1.save('screenshot.png')

                        speak("screen shot saved ")
    else:
                        speak("sorry  screenshot failed ")



def musiccontrol(a):#play,pause,increase-decrease volume,play nxt or prev music. 
    #You have to play the song manually then only you can use these
    if a=='play' :
        pyautogui.press('playpause')

    elif a=='pause':
        pyautogui.press('playpause')

    elif a=='next':
        pyautogui.press('nexttrack')

    elif a=='back':
        pyautogui.press('prevtrack')
        pyautogui.press('prevtrack')

    elif a=='volume up':
        
        pyautogui.press('volumeup',presses=3)

    elif a=='volume down':
        pyautogui.press('volumedown',presses=3)
    
    elif a=="start music":
        subprocess.run("C:\\Users\\HOME\\AppData\\Local\\Microsoft\\WindowsApps\\SpotifyAB.SpotifyMusic_zpdnekdrzrea0\\Spotify.exe",shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True )
    elif a==None:
        pass
    else:
        speak("sorry sir,i can not do that")


def news():
    r=requests.get("https://player.fm/series/bbc-minute")
    soup=BeautifulSoup(r.text,features="lxml")
    data1=soup.find("a",class_="play-prompt playable button",href=True)
    out=subprocess.run("start vlc {}" .format(data1.get("href")),shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True)
    if out.returncode==0:
                time.sleep(64)
                subprocess.run("taskkill /f /im vlc.exe",shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True)
                
    
def switch_task():

    pyautogui.hotkey("alt","tab")
    pyautogui.keyDown("alt")

    while True:
        a=listen()
        if a!=None:
                if a.lower()=="next":
                    pyautogui.press("tab")

                elif a.lower()=="select":
                    pyautogui.keyUp("alt")
                    break
        else:
            pass                  

