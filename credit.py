from tkinter import *


root=Tk()
root.geometry('1000x1000')
root.configure(background="#003d79")
top_frame=Frame(root,width=3000,height=100,pady=20,padx=20,bg="black")
top_frame.pack()
Label(top_frame,text="CREDITS ",font=('Algerian',60,"bold italic"),bg='#ccffff').pack(anchor=CENTER)
Label(root,text='\nCREATED BY: ',font=('Algerian',40,"bold italic")).pack(anchor=CENTER)
Label(root,text='NITYA ANAND & SHEROZ AHMED ',font=('Algerian',40,"bold italic")).pack(anchor=CENTER)
Label(root,text='SUBMITTED TO: ',font=('Algerian',40,"bold italic")).pack(anchor=CENTER)
Label(root,text='JUNAID ALI \n',font=('Algerian',40,"bold italic")).pack(anchor=CENTER)



mainloop()