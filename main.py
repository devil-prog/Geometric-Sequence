import tkinter as tk

#Functions
class app:
    def __init__(self,e1,e2,e3):
        self.e1 = int(e1)
        self.e2 = int(e2)
        self.e3 = int(e3)

    def calculate(self,n):
        if (self.e2/self.e1) == (self.e3/self.e2):
            out = self.e1*((self.e2/self.e1)**(int(n)-1))
            top = tk.Toplevel()
            top.geometry("250x250")
            msg = tk.Label(top, text=out)
            msg.config(font=('Helvetica bold',40))
            msg.pack()
            print(out)

def get_entry_fields():
    a = app(e1.get(),e2.get(),e3.get())
    a.calculate(en.get())     

top = tk.Tk()
#Code to add widgets
#Added lables
tk.Label(top, text="Enter first 3 numbers").grid(row=0)
tk.Label(top, text="Enter Element number").grid(row=1)

#Added entrys
e1 = tk.Entry(top)
e2 = tk.Entry(top)
e3 = tk.Entry(top)
en = tk.Entry(top)

#Organize entrys
e1.grid(row=0, column=1)
e2.grid(row=0, column=2)
e3.grid(row=0, column=3)
en.grid(row=1, column=1)
    
tk.Button(top, text='Submit', command=get_entry_fields).grid(row=3, column=1, sticky=tk.W, pady=4)

top.mainloop()
