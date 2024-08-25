from tkinter import *

root = Tk()
root.geometry("400x300")
def myClick():
    myLabel = Label(root, text="Look! I clicked a button")
    myLabel.pack()

myButton = Button(root, text="Click me!", padx=10, pady=6, command=myClick, fg="white", bg="blue")
myButton.pack()

root.mainloop()