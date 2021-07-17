from tkinter import *
from tkinter import messagebox
import os
import datetime
date=datetime.datetime.now().day
month=datetime.datetime.now().month
year=datetime.datetime.now().year
def menu(event):
    pckg=(variable.get())
def submit(event):
    try:
        pckg=variable.get()
        if pckg=='Golden Package (1000/-)':
            expire=str(date)+'/'+str(month)+'/'+str(year+1)
        elif pckg=='Silver Package (2500/-)':
            expire=str(date)+'/'+str(month)+'/'+str(year+2)
        elif pckg=='Platinum Package (6000/-)':
            expire=str(date)+'/'+str(month)+'/'+str(year+3)
        user_age=int(age.get())
        name1=str(f_name.get())
        name2=str(l_name.get())
        phone=int(phn.get())
        name=name1+' '+name2
        print(name)

    except Exception:
        messagebox.showerror('Wrong Input','Age and phone should only be in number \n Name should not contain numbers!')
        f_name.delete(0,END)
        l_name.delete(0,END)
        age.delete(0,END)
        phn.delete(0,END)

    database_name=open('database_names.txt','a')
    database_age=open('database_age.txt','a')
    database_phone=open('database_phone.txt','a')
    database_pckg=open('database_pckg.txt','a')
    database_expiry=open('database_expiry.txt','a')
    database_name.write(name+'\n')
    database_age.write(str(user_age)+'\n')
    database_phone.write(str(phone)+'\n')
    database_pckg.write(pckg+'\n')
    database_expiry.write(expire+'\n')
    database_age.close()
    database_phone.close()
    database_name.close()
    database_pckg.close()
    f_name.delete(0,END)
    l_name.delete(0,END)
    age.delete(0,END)
    phn.delete(0,END)
def main(event):
    root.destroy()
    os.system('python main_gui_gym.py')

root=Tk()
root.geometry('1000x1000')
root.configure(bg='#003d79')
top_frame=Frame(root,width=1000,height=200,padx=20,pady=20,bg='black')
top_frame.pack()
Label(top_frame,text="NEW USER ",font=('Algerian',45,"bold italic"),bg='#ccffff').pack(anchor=CENTER)
Label(root,text="FIRST NAME: ",font=('Algerian',20,'bold italic'),bg='#ccffff').place(x=40,y=250)
Label(root,text='AGE: ',font=('Algerian',20,'bold italic'),bg='#ccffff').place(x=600,y=250)
Label(root,text="LAST NAME: ",font=('Algerian',20,'bold italic'),bg='#ccffff').place(x=40,y=303)
Label(root,text="PHONE # : ",font=('Algerian',20,'bold italic'),bg='#ccffff').place(x=40,y=358)
Label(root,text='PACKAGE: ',font=('Algerian',20,'bold italic'),bg='#ccffff').place(x=597,y=303)

submit_button=Button(root,text="SUBMIT",font=('Algerian',20,'bold italic'))
submit_button.place(x=400,y=500)
main_menu=Button(root,text="Return to Main Menu",font=('Algerian',12,'bold italic'))
main_menu.place(x=360,y=590)

f_name=Entry(root)
f_name.place(x=250,y=258)
age=Entry(root)
age.place(x=750,y=258)
l_name=Entry(root)
l_name.place(x=250,y=312)
phn=Entry(root)
phn.place(x=250,y=365)
variable=StringVar()
variable.set('Choose Package')
lst=OptionMenu(root,variable,'Golden Package (1000/-)','Silver Package (2500/-)','Platinum Package (6000/-)',command=menu)
lst.place(x=787,y=305)
submit_button.bind("<Button-1>",submit)
main_menu.bind("<Button-1>",main)
# variable.trace('w',menu)

mainloop()