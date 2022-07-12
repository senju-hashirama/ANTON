import subprocess
import mysql.connector as sc
import os



def download_modules():
    os.system("pip install -r requirements.txt")

def books_database():
    password=input("Enter mysql password: ")
    d=open("sql.txt","w")
    d.write(password)
    d.close()

def start():
    os.startfile("window 1.py")

download_modules()
books_database()
check=input("""
i) Download the pyaudio.whl file from https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio
refer this video for installation : https://www.youtube.com/watch?v=-3am_5jMzJ4

ii) Please create a database named projet in sql and run the following command after selecting the databse project <source "path of project_books_dataset.sql file">
press enter to continue

""")
if check=="/n":
    start()
start()


