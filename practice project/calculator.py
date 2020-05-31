from tkinter import *
from tkinter import messagebox

window=Tk()

def plus():
    t1.delete("1.0",END)
    t1.insert(END,float(e1_value.get())+float(e2_value.get()))
def minus():
    t1.delete("1.0",END)
    t1.insert(END,float(e1_value.get())-float(e2_value.get()))
def multi():
    t1.delete("1.0",END)
    t1.insert(END,float(e1_value.get())*float(e2_value.get()))
def division():
    if not float(e1_value.get()) and not float(e2_value.get()) :
        messagebox.showerror("Devine error","You can't devine 0/0")
    elif not float(e2_value.get()):
        messagebox.showerror("Devine error","You can't devine with 0")
    else:
        t1.delete("1.0",END)
        t1.insert(END,float(e1_value.get())/float(e2_value.get()))

l1=Label(window,text="Insert first number")
l1.grid(row=0,column=0)

l2=Label(window,text="Insert second number")
l2.grid(row=0,column=1)

b1=Button(window,text="+",command=plus)
b1.grid(row=0,column=2)

b1=Button(window,text="-",command=minus)
b1.grid(row=0,column=3)

b1=Button(window,text="*",command=multi)
b1.grid(row=1,column=2)

b1=Button(window,text="/",command=division)
b1.grid(row=1,column=3)

e1_value=StringVar()

e1=Entry(window,textvariable=e1_value)
e1.grid(row=1,column=0)

e2_value=StringVar()

e2=Entry(window,textvariable=e2_value)
e2.grid(row=1,column=1)

t1=Text(window,height=1,width=10)
t1.grid(row=1,column=4)

l3=Label(window,text="Result")
l3.grid(row=0,column=4)

window.mainloop()