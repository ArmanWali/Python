from tkinter import *

root = Tk()

# Creating a Label Widget
myLabel1 = Label(root, text="Hello World")
myLabel2 = Label(root, text="My name is Arman Wali")

myLabel1.grid(row=0,column=0) # showing it into the screen
myLabel2.grid(row=1,column=0) # showing it into the screen

root.mainloop()