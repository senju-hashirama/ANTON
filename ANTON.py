#main program
import modules
import os
import subprocess
import time
import plyer
import playlist_maker1
import time
import joeks
from plyer import notification
import datetime

try:
    
    txt=open("config.txt","r")
    data=eval(txt.read())
    txt1=open("mfile.txt","r")
    data1=eval(txt1.read())

    event=open("event.txt","r")
    events=eval(event.read())
    u_name=data["u_name"]
    b_time=data["b_time"]
except FileNotFoundError:

    modules.speak("Please run setup.py file first")
    exit()



def make_playlist():
    if os.path.exists(data1["m_file"]+"/"+"anton_playlist"):
        pass
    else:
        music=os.listdir(data1["m_file"])
        music_lis=[]
        for i in music:
            if ".mp3" or ".m4a" in i:
                music_lis.append(data1["m_file"]+"/"+i)     
        playlist_maker1.create(data1["m_file"]+"/",music_lis,"anton_playlist")
        
def take_break():
    os.startfile("notification.pyw")
def play_music():
    modules.speak("sure thing sir")
    os.startfile(data1["m_file"]+"/"+"anton_playlist.wpl")


#identification of commands takes place here
def identify(a):

    if a in ["anton play my songs","start music","play music","start music","play my songs anton","anton start music","turn on the music","anton turn on the music","turn on the music anton"]:
        
        play_music()
    

    elif a in ["download song","start song downloader","song downloader","music downloader","start music downloader","music downloader music downloader"]:
        modules.speak("starting song downloader "+u_name)
        os.system(r"python music.py")


    elif a .startswith("who")or a.startswith("why") or a.startswith("how") or a.startswith("when"):
        modules.speak("here is what i found")
        modules.google(a)


    elif "google" in a:
        modules.google(a[7:])
        modules.speak("here you go "+u_name)


    elif "youtube" in a :
        modules.youtube(a[7:])
        modules.speak("here you go "+u_name)


    elif a=="stack overflow":
        modules.speak("what should i search for "+u_name)
        data=modules.listen()
        if data !=None:
            
                modules.stack(data)
        else:
            ("sorry sir")


    elif a in ["switch task","switch task anton","which task","which task anton","anton which task","anton switch task"]:
        modules.switch_task()


    elif a in["search wiki" ,"wiki search"]:
        modules.speak("what should i search for "+u_name)
        print(">>")
        data=modules.listen()
        modules.wiki(data)


    elif a in ["volume down","volume up","play","pause","start music","next","back","volume of","play play"]:
        modules.musiccontrol(a)

    
    elif a in ["start music","music"]:
        play_music()


    elif a in ["tell me a joke","joke","tell me a joke anton","antontell me a joke"]:
        modules.speak("here's one "+u_name)
        joeks.get_joke()


    elif a in  ['another one',"one more","tell me another one","one more please","another one and torn","another one hair and tone","another one and on","how about another one","tell me another joke ","another one ringtone"] :
        modules.speak("here you go "+u_name)
        joeks.get_joke()


    elif "take a screenshot" in a :
        modules.screenshot()


    elif a in ["anton read the news","read the news anton","news update","new subject"]:
        modules.speak("Here you go "+u_name)
        modules.news()


    elif a in ["sleep anton","sleep","anton sleep"]:
        out=subprocess.run("rundll32.exe powrprof.dll,SetSuspendState 0,1,0",shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True)


    elif a in ["shutdown","shutdown anton","anton shutdown","power off","anton power off","power off anton"]:
            modules.speak("Shuting down system in five seconds")
            out=subprocess.run("shutdown -f -t 5",shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True)


    elif a in ["random facts","random fact","anton random facts","Brandon Stark","one more fact","another fact","another Stark"]:
        modules.speak(""" here's one """+u_name)
        modules.facts()


    elif a in ["anton i am feeling sad","I am sad and down","I am sad and toned","I am sad ringtone","anton i am feeling low","i am sad and torn","i am sad and tone","anton i am sad ","i am sad anton","i am sad","i am feeling sad","i am feeling low","i am sad danton","I am sad and tone","I am start and tone",]:
        subprocess.run("hugs.gif",shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True)
        modules.speak("you will be alright "+u_name +", let me give you a hugg")
        modules.speak("there, there, there, there ")    

    elif a in ["anton start anime player","anime player","start anime player anton","start animal player","start anime player","animal player"]:
        modules.speak("starting anime player "+u_name)
        os.startfile("animes.py")
    elif a in ["hey anton","hello anton","hi santan","hello Santan","hi don","hello Don","hi hair and tone","hello hair and tone","hello i am tone","hi i am tone","hello ringtone","hi ringtone","hi i am tom","hello i am tom","hi town","hello town","hi i am torn","hello i am torn","hi and turn","hello and turn","hi tom","hello tom","hi up and down","hello and turn"]:
        modules.speak("hello "+u_name)

    elif a in ["what is the time","anton what is the time","is the time"]:
            strTime = datetime.datetime.now().strftime("%H:%M:")   
            modules.speak(f"Sir, the time is {strTime}")
    
    elif a in events: 
        lis=events[a]  
        for i in lis:
            os.startfile(i)
            time.sleep(2)
    elif a in ["reset","anton reset","reset anton"]:
        modules.speak("deleting config files")
        
        os.system("taskkill /f /im pythonw.exe")
        os.system("taskkill /f /im pyw.exe")
        os.startfile("reset.py")
        exit()
        
    else:
        pass

    

#takes audio output

def listen():
    
    a=modules.listen()
    if a !=None:
        
        notification.notify(
            title="A.N.T.O.N",
            message=a,
            timeout=5)
        if a.lower() in ["hey anton","Santan","Don","hair and tone","and on","I am town","I am tone","antonym","wake up","anton wake up","wake up anton","hey buudy","anton anton","anton","and town","antonyms","ringtone","and tone","i am tom","town","i am torn","i talk","and turn","tom","wake up and down","up and down","wake up and turn"]:
            modules.speak("yes "+u_name)
            
        else:
            identify(a.lower())




#driver program
make_playlist()
modules.speak("Hello "+u_name)
take_break()
while True:
    listen()
