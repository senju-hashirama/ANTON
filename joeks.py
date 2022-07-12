#joeks
import requests
from bs4 import BeautifulSoup
import modules
import time

from plyer import notification
#functions
def get_joke():
        data1=requests.get("https://sv443.net/jokeapi/v2/joke/any")

        data=data1.json()
        

        if data["category"]!="Dark":

            if data["type"]== "twopart":
                
                notification.notify(
            title="A.N.T.O.N",
            message=data["setup"],
            timeout=3)
                modules.speak(data["setup"])
                
                
                notification.notify(
            title="A.N.T.O.N",
            message=data["delivery"],
            timeout=4)
                modules.speak(data["delivery"])
            else:
                notification.notify(
            title="A.N.T.O.N",
            message=data["delivery"],
            timeout=4)
                modules.speak(data["joke"])
        else:
            get_joke()
            
