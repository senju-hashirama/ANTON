from pyDes import *
import base64
import requests
import wget
from tkinter import filedialog
from tkinter import Tk
from pathlib import Path
import playsound
import os.path
#decryption
des_cipher = des(b"38346591", ECB, b"\0\0\0\0\0\0\0\0" , pad=None, padmode=PAD_PKCS5)
base_url = 'http://h.saavncdn.com'
def decrypt_url(url):
    enc_url = base64.b64decode(url.strip())
    dec_url = des_cipher.decrypt(enc_url,padmode=PAD_PKCS5).decode('utf-8')
    dec_url = base_url + dec_url.replace('mp3:audios','')
    a=input("do you want to play or download the song:p/d")
    if a=="p":
        try:
            os.system("start vlc "+dec_url[21:])
        except:
            print("please check if vlc is installed")
    else:
        download(dec_url[21:])
    
		
#download
def download(url):
    if os.path.exists("mfile.txt"):
         d=open("mfile.txt","r")
         dic=eval(d.read())
         filename=dic["m_file"]
         print(filename)
         song_path=filename+"/"+song_name+".mp3"
         wget.download(url,song_path)
         
         
    else:
         tk=Tk()
         Tk.withdraw(tk)
         filename=filedialog.askdirectory()
         print(filename)
         a=open("mfile.txt","w")
         a.write(filename)
         song_path=filename+"/"+song_name+".mp3"
         print(song_path)
         wget.download(url,song_path)
         
     
def search(a):
    lis=a.split(" ")
    string=""
    for i in lis:
        string=string+i+"+"
    
    search="https://www.jiosaavn.com/api.php?p=1&q={}&_format=json&_marker=0&api_version=4&ctx=wap6dot0&n=20&__call=search.getResults" .format(string)
    r=requests.get(search)
    dic=r.json()
    results=dic["results"]
    for i in range (len(results)):
        print(i+1,"Song name:",results[i]["title"])
        print(results[i]["subtitle"])
        print("""
""")

    s_no=int(input("Enter song number: "))
    
    e_url=results[s_no-1]["more_info"]["encrypted_media_url"]
    global song_name
    song_name=results[s_no-1]["title"]
    decrypt_url(e_url)
    
    
print("""


'                              _                                          
'     ____ ___   __  __ _____ (_)_____                                    
'    / __ `__ \ / / / // ___// // ___/                                    
'   / / / / / // /_/ /(__  )/ // /__                                      
'  /_/ /_/_/_/ \__,_//____//_/ \___/__                   __               
'    ____/ /____  _      __ ____   / /____   ____ _ ____/ /___   _____    
'   / __  // __ \| | /| / // __ \ / // __ \ / __ `// __  // _ \ / ___/    
'  / /_/ // /_/ /| |/ |/ // / / // // /_/ // /_/ // /_/ //  __// /        
'  \__,_/ \____/ |__/|__//_/ /_//_/ \____/ \__,_/ \__,_/ \___//_/         
'                                                                         
                                                                -the_silent_guardian
""")
song=input("Enter song name : ")
search(song)     
