from tkinter import *
from tkinter import messagebox
import os
def back():
    root.destroy()
    os.system('python data_gym.py')
def opt(event):
    variable.get()

name_file=open('database_names.txt','r')
phone_file=open('database_phone.txt','r')
age_file=open('database_age.txt','r')
expire_file=open('database_expiry.txt','r')
database=[]
id_user=1
i=0
while True:
    print('inside',i)
    name=name_file.readline()
    if name=="":
        break
    else:
        name=name[0:-1]
        phone=phone_file.readline()
        phone=phone[0:-1]
        age=age_file.readline()
        age=age[0:-1]
        expire=expire_file.readline()
        expire=expire[0:-1]
        x={}
        x["name"]=name
        x['phone']=phone
        x['age']=age
        x['id']=str(id_user+i)
        x['expire']=expire
        database.append(x)
        i+=1
print(database)
name_file.close()
age_file.close()
phone_file.close()
expire_file.close()
def search_data(to_search,database):
    j=0
    for i in range(len(database)):
        if to_search in database[i]['id']:
            print(i)
            print("searched")
            Label(root,text=database[i]['id'],width=10,bg='grey').place(x=2,y=500+25*j)
            Label(root,text=database[i]['name'],width=47,bg='grey').place(x=90,y=500+25*j)
            Label(root,text=database[i]['age'],width=9,bg='grey').place(x=433,y=500+25*j)
            Label(root,text=database[i]['phone'],width=26,bg='grey').place(x=509,y=500+25*j)
            Label(root,text=database[i]['expire'],width=38,bg='grey').place(x=710,y=500+25*j)
            return int(database[i]["id"])
            j+=1
        elif i==len(database)-1:
            Label(root,text='---------NOT FOUND------------',width=131).place(x=2,y=525)
def delete(idd):
    name_file=open('database_names.txt','w')
    phone_file=open('database_phone.txt','w')
    age_file=open('database_age.txt','w')
    expire_file=open('database_expiry.txt','w')
    database.pop(idd-1)
    print(database)
    for i in range(len(database)):
        name_file.write(database[i]['name']+'\n')
        age_file.write(database[i]['age']+'\n')
        phone_file.write(database[i]['phone']+'\n')
        expire_file.write(database[i]['expire']+'\n')
    print(database)
    name_file.close()
    age_file.close()
    phone_file.close()
    expire_file.close()
    messagebox.showinfo('DONE',"User Removed Successfully")
    root.destroy()
    os.system('python modify.py')
def search(event):
    to_search=search_get.get()
    idd=search_data(to_search,database)
    del_button=Button(root,text='delete',command=lambda: delete(idd))
    del_button.place(x=300,y=300)

root=Tk()
root.geometry('1000x1000')
root.configure(background="#003d79")
Label(root,text="EDITING ",font=('Algerian',45,"bold italic"),bg='#71b8ff').place(x=350,y=20)
Label(root,text='SEARCH BY  ',font=('Algerian',20,"bold italic")).place(x=10,y=200)
variable=StringVar()
variable.set('Choose')
Label(root,text='id  ',font=('Algerian',20,"bold italic")).place(x=10,y=300)
search_get=Entry(root)
search_get.place(x=120,y=307)
go=Button(root,text='GO')
go.place(x=250,y=305)
go.bind('<Button-1>',search)
Button(root,text='<---BACK TO DATABASE',command=back).place(x=1,y=1)





mainloop()
