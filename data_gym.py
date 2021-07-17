from tkinter import *
import os
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
def modify():
    root.destroy()
    os.system('python modify.py')
def opt(event):
    print(variable.get())
def menu(event):
    root.destroy()
    os.system('python main_gui_gym.py')
def back(event):
    root.destroy()
    os.system('python data_gym.py')
def search_data(to_search,database,bottom_frame,for_search):
    bottom_frame=Frame(root,width=2000,height=2000,bg="#003d79")
    bottom_frame.pack()
    j=0
    for i in range(len(database)):
        if to_search in database[i][for_search]:
            print(i)
            print("searched")
            Label(bottom_frame,text=database[i]['id'],width=10).place(x=2,y=3+25*j)
            Label(bottom_frame,text=database[i]['name'],width=47).place(x=90,y=3+25*j)
            Label(bottom_frame,text=database[i]['age'],width=9).place(x=433,y=3+25*j)
            Label(bottom_frame,text=database[i]['phone'],width=26).place(x=509,y=3+25*j)
            Label(bottom_frame,text=database[i]['expire'],width=27).place(x=710,y=3+25*j)
            j+=1

    return_list=Button(root,text='<--back')
    return_list.place(x=1,y=30)
    return_list.bind('<Button-1>',back)
def search(event):
    to_search=search_entry.get()
    bottom_frame.destroy()
    for_search=variable.get()
    search_data(to_search,database,bottom_frame,for_search)



root=Tk()
# database=[{'name':'anand','id':1,'phone':'03369895414','expire':'12/12/19','age':18},{'name':'sudha','id':2,'phone':'033698','expire':'2/12/19','age':18},{'name':'daniyal','id':3,'phone':'0336934238','expire':'2/12/19','age':18},{'name':'sudha','id':4,'phone':'033698','expire':'2/12/19','age':18}]

root.geometry('1000x1000')
root.configure(background="#003d79")
top_frame=Frame(root,width=3000,height=1200,pady=20,padx=20,bg="black")
top_frame.pack()
toptext=Label(top_frame,text="DATABASE ",font=('Algerian',45,"bold italic"),bg='#ccffff')
toptext.pack(anchor=CENTER)
mid_frame=Frame(root,width=3000,height=50,bg="black").pack()
bottom_frame=Frame(root,width=2000,height=2000,bg="#003d79")
bottom_frame.pack()
Button(mid_frame,text="ID",bg="#ccffff",width=10,height=2).place(x=2,y=115)
Button(mid_frame,text="NAME",bg="#ccffff",width=50,height=2).place(x=80,y=115)
Button(mid_frame,text='AGE',bg='#ccffff',width=9,height=2).place(x=430,y=115)
Button(mid_frame,text="PH #",bg="#ccffff",width=30,height=2).place(x=500,y=115)
Button(mid_frame,text="PACKAGE-EXPIRY",bg="#ccffff",width=40,height=2).place(x=700,y=115)

Label(root,text="_____________|SEARCH BY|_______________",bg='#ccffff').place(x=730,y=10)
variable=StringVar()
variable.set('Choose')
lst=OptionMenu(root,variable,'phone','id','age','name',command=opt)
lst.place(x=705,y=40)


for i in range(len(database)):
    id_label=Label(bottom_frame,text=database[i]['id'],width=10)
    id_label.place(x=2,y=2+25*i)
    name_label=Label(bottom_frame,text=database[i]['name'],width=47)
    name_label.place(x=90,y=2+25*i)
    age_label=Label(bottom_frame,text=database[i]['age'],width=9)
    age_label.place(x=433,y=2+25*i)
    ph_label=Label(bottom_frame,text=database[i]['phone'],width=26)
    ph_label.place(x=509,y=2+25*i)
    pkg_label=Label(bottom_frame,text=database[i]['expire'],width=38)
    pkg_label.place(x=710,y=2+25*i)


search_entry=Entry(root)
search_entry.place(x=800,y=42)
go=Button(root,text='GO')
go.place(x=940,y=40)
go.bind('<Button-1>',search)
Button(root,text='EDIT DATABASE',command=modify).place(x=800,y=80)

main_menu=Button(root,text="<----Go to Main Menu")
main_menu.place(x=1,y=5)
main_menu.bind('<Button-1>',menu)

mainloop()