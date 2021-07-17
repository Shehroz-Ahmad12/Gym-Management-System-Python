from tkinter import *
from tkinter import messagebox
import os

def submit(event):
    print("getting")
    login=login_entry.get()
    password=password_entry.get()
    if login=="anand" and password=="anand":
        root.destroy()
        os.system('python main_gui_gym.py')
    else:
        login_entry.delete(0,END)
        password_entry.delete(0,END)
        messagebox.showerror('Wrong Input','INCORRECT User Name or Password')


root=Tk()

top_frame=Frame(root)
bottom_frame=Frame(root)
top_frame.pack()
bottom_frame.pack(side=BOTTOM)
img=PhotoImage(file="gymlogo.png")
pic=Label(top_frame,width=300,height=300,image=img)
pic.pack()


username_label=Label(bottom_frame,text="USERNAME: ",bd=10)
password_label=Label(bottom_frame,text="PASSWORD: ",bd=10)
username_label.grid(row=0,column=0)
password_label.grid(row=1,column=0)


login_entry=Entry(bottom_frame)
password_entry=Entry(bottom_frame,show="*")
login_entry.grid(row=0,column=1)
password_entry.grid(row=1,column=1)

submit_button=Button(bottom_frame,text="SUBMIT")
submit_button.grid(columnspan=2)
submit_button.bind('<Button-1>',submit)

mainloop()