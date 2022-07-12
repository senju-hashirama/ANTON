from tkinter import *
from PIL import ImageTk,Image
from tkinter import filedialog
from pathlib import Path
import os

window=Tk()
window.title( "A.N.T.O.N")
window.minsize(width=700,height=450)
window.resizable(0, 0)
def make_config():
    a=open("mfile.txt","w")
    lis=["m_file"]
    lis2=[folder_selected]
    dic=dict(zip(lis,lis2))
    a.write(str(dic))
    a.close()
    os.startfile( "new_window.py" )  
    exit()



def choose_file():
    global folder_selected
    folder_selected = filedialog.askdirectory()
    print(folder_selected)
    
def choose_dfile():
    global dfile
    dfile=filedialog.askdirectory()
    print(dfile)


bg_image=ImageTk.PhotoImage(Image.open("bg1.jpg"))
canvas=Canvas(window,width=1000, height=500)



lable2=Label(window,text="A.N.T.O.N",fg="white",bg="grey",font=("Leelawade",45))
lable2.place(x=400,y=10)

label3=Label(window,text="Where should we look for audio files :",fg="white",bg="grey",font=("Leelawade ",25))
label3.place(x=10,y=300)


button1=Button(text="Choose folder",command=choose_file,font=("Leelawade ",25))
button1.place(x=630,y=300)




button3 =Button(window,text="NEXT",fg="white",bg="grey7",command=make_config,font=("leelawade",20))
button3.place(x=400,y=400)

canvas.create_image(0,0, anchor=NW,image=bg_image)
canvas.pack()

window.mainloop()
