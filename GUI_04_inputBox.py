from tkinter import *
root = Tk()
root.geometry("400x300")

e = Entry(root, width=50, bg="light Pink", fg="white")
e.pack()
e.insert(0, "Enter your Name: ")

def myClick():
    Hello = "Hello " + e.get()
    myLabel = Label(root, text=Hello)
    myLabel.pack()

myButton = Button(root, text="Enter Your Name", command=myClick)
myButton.pack()

root.mainloop()