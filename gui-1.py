import tkinter as tk
from tkinter import ttk
import backend
import frontend
from PIL import ImageTk,Image
w=tk.Tk()
w.title("BOOKS")
w.iconbitmap(r"C:\Users\HOME\Downloads\icon2.ico")
w.minsize(540,480)
w.maxsize(540,480)
bg_image=ImageTk.PhotoImage(Image.open("books.jpg"))
canvas=tk.Canvas(w,width=540, height=480)
gb={}

def filterfunc():
    frontend.execute(gb)

def authors():
    def f():
        s=str(k.get())
        gb['author']=s
    k=tk.StringVar()
    l1=tk.Label(w,text='Author : ',font=('Lucida',12))
    l1.place(x=0,y=5)
    auth=ttk.Combobox(w,textvariable=k)
    auth.place(x=100,y=5)
    auth['values']=tuple(backend.final_list_authors)
    auth.current(0)
    b1=tk.Button(w,text='save',command=f)
    b1.place(x=250,y=5)

def years():
    def f():
        s=str(k.get())
        gb['year']=s
    k=tk.StringVar()
    l2=tk.Label(w,text='Year : ',font=('Lucida',12))
    l2.place(x=0,y=100)
    yrs=ttk.Combobox(w,textvariable=k)
    yrs.place(x=100,y=100)
    yrs['values']=tuple(backend.final_list_years)
    yrs.current(0)
    b1=tk.Button(w,text='save',command=f)
    b1.place(x=250,y=100)

def language():
    def f():
        s=str(k.get())
        gb['lang']=s
    k=tk.StringVar()
    l3=tk.Label(w,text='Language : ',font=('Lucida',12))
    l3.place(x=0,y=200)
    langs=ttk.Combobox(w,textvariable=k)
    langs.place(x=100,y=200)
    langs['values']=tuple(backend.final_list_lang)
    langs.current(0)
    b1=tk.Button(w,text='save',command=f)
    b1.place(x=250,y=200)

def ratings():
    def f():
        s=str(k.get())
        gb['rating']=s
    k=tk.StringVar()
    l4=tk.Label(w,text='Rating : ',font=('Lucida',12))
    l4.place(x=0,y=300)
    r=ttk.Combobox(w,textvariable=k)
    r.place(x=100,y=300)
    r['values']=tuple(backend.final_list_ratings)
    r.current(0)
    b1=tk.Button(w,text='save',command=f)
    b1.place(x=250,y=300)

def rem():
    gb['author']='-none-'
    gb['year']='-none-'
    gb['lang']='-none-'
    gb['rating']='-none-'

rem()
authors()
language()
years()
ratings()
b2=tk.Button(w,text='reset',command=rem)
b2.place(x=410,y=450)
b=tk.Button(w,text='submit',command=filterfunc)
b.place(x=450,y=450)
q=tk.Button(w,text='exit',command=w.destroy)
q.place(x=10,y=450)
canvas.create_image(0,0, anchor="nw",image=bg_image)
canvas.pack()

w.mainloop()
