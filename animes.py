import subprocess
import requests
from bs4 import BeautifulSoup
import os
#import anime


def make_url(a):
		search_url="https://gogoanime.pe//search.html?keyword={}"
		search_item=""
		for i in a.split(" "):
				search_item=search_item+i+"+"
		search_url=search_url.format(search_item)
		get_data(search_url)
def get_data(a):
		dic={}
		r=requests.get(a)
		soup=BeautifulSoup(r.text,features="xml")
		raw_data=soup.find("div",class_="last_episodes")
		name=raw_data.find_all("p",class_="name")
		for i in range(len(name)):
				link=name[i].find("a")
				dic[i+1]=link["href"][9:]
				print(i+1,"   ",name[i].text)
		if len(dic)==0:
				print("Sorry please try again :(")
		else:
				usr_input=int(input(">>>"))
				if usr_input in dic:
						print(dic[usr_input])
						make_video_url(dic[usr_input])
				else:
						print("Invalid option!!")

def make_video_url(a):
		base_url="https://gogoanime.pe{}-episode-{}"
		
		if "movie" in a:
				ep=1
		else:
				ep=input("Enter episode number: ")
		print(base_url.format(a,ep))
		r=requests.get(base_url.format(a,ep))
		soup=BeautifulSoup(r.text,features="xml")
		d=soup.find("li",class_ ="dowloads")
		link=d.find("a")
		
		d_link=link["href"]
		print(d_link)
		get_download_links(d_link,ep,a)

def get_download_links(a,b,c):
		a_name=c.replace("/","+")
		i_start=a.find("=")+1
		i_end=a.find("==")
		ep=b
		m_id=a[i_start:i_end]
		
				# https://streamani.net/download?id=NDQ4MDI=&typesub=Gogoanime-SUB&title=Tokyo+Ghoul+Episode+1
		base_url="https://streamani.net/download?id={}&typesub=Gogoanime-SUB&title={}+{}".format(m_id,a_name,ep)
		

		r=requests.get(base_url)
		soup=BeautifulSoup(r.text,features="xml")
		d=soup.find_all("div",class_ ="dowload")
		lis=[]

		
		print("\n")   
		for i in d:
					link=i.find("a")
				
					if "480" or "360" in link.text:
						
						try:
					
						
								print("PLAYING")
								print(link["href"])

								d=subprocess.run(" vlc "+"\""+link["href"]+"\"",shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
								print(d.stdout)
								h1=open("history.txt","r")
								check=h1.readlines()
								if a_name and ep in check[-1]:
														pass
								else:
										h_file=open("history.txt","a")
										h_file.write(a_name+" "+str(ep)+"  "+link["href"]+"\n")
										h_file.close()
						except :
							break
							
							
							
					
				
if os.path.exists("history.txt"):
		pass
else:
		txt=open("history.txt","w")
		txt.close()
print("""
   ___        _                                
  / _ | ___  (_)_ _  ___                       
 / __ |/ _ \/ /  ' \/ -_)                      
/_/ |_/_//_/_/_/_/_/\__/                       
	 __                __             __       
 ___/ /__ _    _____  / /__  ___ ____/ /__ ____
/ _  / _ \ |/|/ / _ \/ / _ \/ _ `/ _  / -_) __/
\_,_/\___/__,__/_//_/_/\___/\_,_/\_,_/\__/_/   
""")
print("""
' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' '  ' ' ' ' ' '     
' This program can play almost any anime provided vlc media player is installed  '                     '
' If the program does not return any search result check your spelling or        '
' try using the japanese name of the anime                                       '
' If you are searching for a movie then type 1 if prompted for episode number    '                                                                              '
' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' """ )
print("\n")
while True:
		a=input("""Enter anime name or exit to close the program
>>>""")

		if a=="exit":
				print("Thank you (-_-)")
				break
		make_url(a)
#https://gogo-stream.com/download?id=MTMxNDk0&typesub=Gogoanime-DUB&title=One+Punch+Man+2nd+Season+%28Dub%29+Episode+1

