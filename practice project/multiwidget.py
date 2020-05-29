from tkinter import *

window=Tk()

l1=Label(window,text="Kg",height=1,width=20)
l1.grid(row=0,column=0)

e1_value=StringVar()

e1 = Entry(window,textvariable=e1_value)
e1.grid(row=0,column=1)

b1=Button(window,text="Convert",height=1,width=20)
b1.grid(row=0,column=2)

window.mainloop()