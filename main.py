import tkinter as tk
class app:
    def __init__(self,e1,e2,e3):
        self.e1 = e1
        self.e2 = e2
        self.e3 = e3

    def get_entry_fields():
        a = e1
        b = e2
        c = e3
        print(a,b,c)
top = tk.Tk()
# Code to add widgets
tk.Label(top, text="Enter first 3 numbers").grid(row=0)

e1 = tk.Entry(top)
e2 = tk.Entry(top)
e3 = tk.Entry(top)

e1.grid(row=0, column=1)
e2.grid(row=0, column=2)
e3.grid(row=0, column=3)

tk.Button(top, text='Submit', command=lambda:[app(e1.get(), e2.get(), e3.get()), app.get_entry_fields()]).grid(row=3, column=1, sticky=tk.W, pady=4)
#app(e1.get(), e2.get(), e3.get())



'''def helloCallBack():
        print( "Hello Python", "Hello World")

        B = tk.Button(top, text ="Hello", command = helloCallBack)

        B.pack()'''

top.mainloop()
