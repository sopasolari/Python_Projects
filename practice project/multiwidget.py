from tkinter import *

window=Tk()

def convert():
    t1.insert(END,float(e1_value.get())*1000)
    t2.insert(END,float(e1_value.get())*2.2046)
    t3.insert(END,float(e1_value.get())*35.274)

l1=Label(window,text="Kg",height=1,width=20)
l1.grid(row=0,column=0)

e1_value=StringVar()

e1 = Entry(window,textvariable=e1_value)
e1.grid(row=0,column=1)

b1=Button(window,text="Convert",height=1,width=10,command=convert)
b1.grid(row=0,column=2)

t1=Text(window,height=1,width=20)
t1.grid(row=1,column=0)

t2=Text(window,height=1,width=20)
t2.grid(row=1,column=1)

t3=Text(window,height=1,width=20)
t3.grid(row=1,column=2)

window.mainloop()