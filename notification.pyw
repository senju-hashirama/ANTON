import time
from plyer import notification
import pyttsx3


def speak(text):#uses pyttsx3 and sapi5 engine to convert text to speech
    engine=pyttsx3.init("sapi5")#change this if on other os other than windows 
    engine.setProperty('rate',170)
    engine.setProperty('volume', '1')
    engine.say(text)
    engine.runAndWait()
   
txt=open("config.txt","r")
data=eval(txt.read())
u_name=data["u_name"]
b_time=data["b_time"]
x=u_name+" you have been using the pc for "+str(b_time)+" minutes, you should take a break"
tim=int(b_time)*60


while True:
        time.sleep(int(tim))
        notification.notify(
            title="A.N.T.O.N",
            message=x,
            app_icon="C:\\Users\\HOME\\Downloads\\icon1.ico",
            timeout=5)
        speak(x)
