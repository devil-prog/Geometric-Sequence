import tkinter as tk
from tkinter import *
import sys

#Functions
class app:
    def __init__(self,e1,e2,e3):
        self.e1 = int(e1)
        self.e2 = int(e2)
        self.e3 = int(e3)

    def calculate(self,n):
        if (self.e2/self.e1) == (self.e3/self.e2):
            try:
                out = self.e1*((self.e2/self.e1)**(int(n)-1))
            except:
                print("Oops!", sys.exc_info()[0], "occurred.")
                print("Next entry.")
                print()
            if 10000000000000000 > out:
                top = tk.Toplevel()
                top.geometry("720x72")
                msg = tk.Label(top, text=out)
                msg.config(font=('Helvetica bold', 40))
                msg.pack()
                print(out)
            else:
                print(out)

    def calculate2(self,Tn):
        if (self.e2/self.e1) == (self.e3/self.e2):
            try:
                st1 = int(Tn)/self.e1
            except:
                print("Oops!", sys.exc_info()[0], "occurred.")
                print("Next entry.")
                print()
            r = (self.e2/self.e1)
            i = 1
            j = r
            while 10000000000000000 > r:
                r = r*j
                i = i+1
                if r == st1:
                    out = i+1
                    top = tk.Toplevel()
                    top.geometry("720x72")
                    msg = tk.Label(top, text=out)
                    msg.config(font=('Helvetica bold',40))
                    msg.pack()
                    print(out)
                    break
                if r > st1:
                    print("This number is not in the sequence")
                    break
                
            
def get_entry_fields():
    a = app(e1.get(),e2.get(),e3.get())
    if not en.get():
        a.calculate2(eTn.get())
    else:
        a.calculate(en.get())
            

top = tk.Tk()
top.title("Geometric-Sequence")
p1 = PhotoImage(file = 'icon.png')
top.iconphoto(False, p1)

#Code to add widgets
#Added lables
tk.Label(top, text="Enter first 3 numbers").grid(row=0)
tk.Label(top, text="To Find Value of Element",).grid(row=1,column=2)
tk.Label(top, text="Enter Element number").grid(row=2)
tk.Label(top, text="To Find Element of Given Value").grid(row=3,column=2)
tk.Label(top, text="Enter Element value").grid(row=4)

#Added entrys
e1 = tk.Entry(top)
e2 = tk.Entry(top)
e3 = tk.Entry(top)
en = tk.Entry(top)
eTn = tk.Entry(top)

#Organize entrys
e1.grid(row=0, column=1)
e2.grid(row=0, column=2)
e3.grid(row=0, column=3)
en.grid(row=2, column=1)
eTn.grid(row=4, column=1)

row, column = top.grid_size()    
tk.Button(top, text='Submit', command=get_entry_fields).grid(row=row+1, column=column, sticky=tk.NS, padx=20, pady=20)

top.mainloop()
