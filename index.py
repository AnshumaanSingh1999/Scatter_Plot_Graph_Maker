from tkinter import *
from tkinter import ttk, filedialog
from tkinter.filedialog import askopenfile
from tkinter import messagebox
import sys
import os
import subprocess


root = Tk()

filepath=""


root.title("Testing")
root.geometry('350x200')


lbl = Label(root, text = "Plot:")
lbl.grid()
res=Label(root)
res.grid(column=1,row=0)


# btn1 = Button(root, text ='Select File', command = lambda:open_file())
# btn1.grid(column=2, row=0)

btn = Button(root, text = "Visualise" , fg = "red", command=lambda:run())
btn.grid(column=3, row=0)

# btnr = Button(root, text = "Refresh" , fg = "red", command=lambda:refresh())
# btnr.grid(column=4, row=0)


def run():

    subprocess.call(["python", "test.py"])
            
		



	
root.mainloop()