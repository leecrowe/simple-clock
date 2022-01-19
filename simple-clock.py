from tkinter import *
from tkinter.ttk import *
from time import strftime

root = Tk()
root.title("Simple Clock")

label = Label(root, font=("Arial", 66), background = "white", foreground = "black")
label.pack(anchor = 'center')

def time():
  string = strftime('%I:%M:%S%p')
  label.config(text=string)
  label. after(1000, time)
  
time()
mainloop()