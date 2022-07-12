from tkinter import *
from PIL import ImageTk,Image
import subprocess
from tkinter import filedialog
from pathlib import Path
import os


y_co=255
path_lis=[]
e_count=0


window=Tk()
window.title( "A.N.T.O.N")
window.minsize(width=500,height=500)
window.resizable(0, 0)
def make_config():
    a=open("event.txt","w")
    lis=entry2.get()
    lis2=path_lis
    dic={lis:lis2}
    a.write(str(dic))
    a.close()
    os.startfile("ANTON.py")
    exit()



def choose_file():
    global folder_selected
    folder_selected = filedialog.askopenfilename()
    path_lis.append(folder_selected)
    
def button_init():
    global y_co    
    label4=Label(window,text="->APP",fg="white",bg="grey7",font=("Leelawade ",14))
    label4.place(x=10,y=y_co+20)

    button2=Button(text="Select",command=choose_file)
    button2.place(x=100,y=y_co+20)
    
    y_co=y_co+30
def add_event():
    os.startfile("window 3.py")
    make_config()


bg_image=ImageTk.PhotoImage(Image.open("bg.jpeg"))
canvas=Canvas(window,width=500, height=500)



lable2=Label(window,text="A.N.T.O.N",fg="white",bg="grey7",font=("Leelawade",45))
lable2.place(x=100,y=10)



label3=Label(window,text="->set up events:",fg="white",bg="grey7",font=("Leelawade ",16))
label3.place(x=10,y=150)

label3=Label(window,text="->Name",fg="white",bg="grey7",font=("Leelawade ",16))
label3.place(x=10,y=200)

entry2=Entry(window)
entry2.place(x=100,y=205)

label4=Label(window,text="->APP",fg="white",bg="grey7",font=("Leelawade ",14))
label4.place(x=10,y=240)

button2=Button(text="Select",command=choose_file)
button2.place(x=100,y=245)

button3=Button(text="add event",command=add_event,fg="white",bg="grey7",font=("leelawade",20))
button3.place(x=300,y=430)


button4=Button(text="ADD",command=button_init,fg="white",bg="grey7",font=("leelawade",20))
button4.place(x=200,y=430)

button2 =Button(window,text="save",fg="white",bg="grey7",command=make_config,font=("leelawade",20))
button2.place(x=100,y=430)

canvas.create_image(0,0, anchor=NW,image=bg_image)
canvas.pack()

window.mainloop()
