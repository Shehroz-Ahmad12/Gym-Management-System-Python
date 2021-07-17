from tkinter import *
from tkinter import messagebox
import sys
import os
import time

def exiting(event):
    root.destroy()
def show_users(event):
    root.destroy()
    os.system('python data_gym.py')
def adding(event):
    root.destroy()
    os.system('python adduser_gym.py')
def credit():
    root.destroy()
    os.system('python credit.py')
root=Tk()
root.geometry('1000x1000')
root.configure(background="#003d79")
top_frame=Frame(root,width=3000,height=100,pady=20,padx=20,bg="black")
top_frame.pack()
toptext=Label(top_frame,text="MAIN MENU ",font=('Algerian',60,"bold italic"),bg='#ccffff')
toptext.pack(anchor=CENTER)

bottom_frame=Frame(root,width=3000,height=500,padx=30,pady=30,bg="black")
bottom_frame.place(x=230,y=250)

Button1=Button(bottom_frame,width=30,height=2,text="ADD NEW USER",font=('Castellar',15,"bold italic"),bg='#ccffff')
Button1.pack(side=TOP,anchor=CENTER)
Button2=Button(bottom_frame,width=30,height=2,text="SHOW ALL USERS",font=('Castellar',15,"bold italic"),bg='#ccffff')
Button2.pack(anchor=CENTER)
Button3=Button(bottom_frame,width=30,height=2,text="CREDITS",font=('Castellar',15,"bold italic"),bg='#ccffff',command=credit)
Button3.pack(anchor=CENTER)
Button4=Button(bottom_frame,width=30,height=2,text="QUIT",font=('Castellar',15,"bold italic"),bg='#ccffff')
Button4.pack(side=TOP,anchor=CENTER)

Button4.bind('<Button-1>',exiting)

Button2.bind('<Button-1>',show_users)
Button1.bind('<Button-1>',adding)
mainloop()