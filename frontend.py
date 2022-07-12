import mysql.connector as msc
import tkinter as tk
d=open("sql.txt","r")

password=d.read()
d.close()
ref=[]
con=msc.connect(host='localhost',user='root',passwd=password,database='project')
cur=con.cursor()
txt=''

def send():
    nw=tk.Tk()
    nw.minsize(300,250)
    nw.maxsize(600,600)
    for i in ref:
        if txt in i:
            l=tk.Label(nw,text=i[0])
            l.grid(row=0,column=1)
            for j in range(1,10):
                ll=tk.Label(nw,text=i[j])
                ll.grid(row=j%3,column=j//3)
            else:
                break
            
    nw.mainloop()

def win(d):
    wi=tk.Tk()
    wi.minsize(1440,720)
    wi.maxsize(1440,720)
    k=0
    global txt
    for i in d:
        txt=i[5]
        b=tk.Button(wi,text=txt,command=send)
        b.grid(row=k%15,column=k//15)
        k+=1
    wi.mainloop()

def execute(query):
    temp=query
    op='select * from books_dataset where '
    if len(temp)>1:
        if temp['author']!='-none-':
            op+='author like "%'+temp['author']+'%" and '
        if temp['year']!='-none-':
            op+='publication_year='+str(temp['year'])+' and '
        if temp['lang']!='-none-':
            op+='language like "%'+temp['lang']+'%" and '
        if temp['rating']!='-none-':
            op+='avg_rating>'+str(temp['rating'])+' and '
        if op[-4:]=='and ' :
            op=op[:-4]+';'
    else:
        if temp['author']!='-none-':
            op+='author like "%'+temp['author']+'%";'
        elif temp['year']!='-none-':
            op+='publication_year='+str(temp['year'])+';'
        elif temp['lang']!='-none-':
            op+='language like "%'+temp['lang']+'%";'
        elif temp['rating']!='-none-':
            op+='avg_rating>='+str(temp['rating'])+';'
    cur.execute(op)
    data=cur.fetchall()
    global ref
    ref=data
    win(data)
