from tkinter import *
from PIL import ImageTk,Image
import subprocess
import os

window=Tk()
window.title( "A.N.T.O.N")
window.minsize(width=500,height=500)
window.resizable(0, 0)
def make_config():
    a=open("config.txt","w")
    lis=["u_name","b_time",]
    lis2=[entry2.get(),
    entry3.get()]
    dic=dict(zip(lis,lis2))
    a.write(str(dic))
    a.close()
    os.startfile( "window 2.py" )  
    exit()


bg_image=ImageTk.PhotoImage(Image.open("bg.jpeg"))
canvas=Canvas(window,width=870, height=500)



lable2=Label(window,text="A.N.T.O.N",fg="white",bg="grey7",font=("Leelawade",45))
lable2.place(x=300,y=10)



label3=Label(window,text="What should the assistant call you :",fg="white",bg="grey7",font=("Leelawade ",22))
label3.place(x=10,y=200)

entry2=Entry(window,font=("Leelawade ",17))
entry2.place(x=480,y=205)

label4=Label(window,text="Remind me to take a break after(in minutes):",fg="white",bg="grey7",font=("Leelawade ",22))
label4.place(x=10,y=300)

entry3=Entry(window,text="60",font=("Leelawade ",17))
entry3.place(x=600,y=305)


button2 =Button(window,text="NEXT",fg="white",bg="grey7",command=make_config,font=("leelawade",20))
button2.place(x=400,y=400)

canvas.create_image(0,0, anchor=NW,image=bg_image)
canvas.pack()

window.mainloop()
