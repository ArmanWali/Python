from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('image viewer')

root.iconbitmap('E:/HTML & CSS/icons/crown.ico') # icon at the start of a title

my_img = ImageTk.PhotoImage(Image.open("E:/HTML & CSS/icons/giki.png"))
my_label = Label(image = my_img)

my_label.pack()

button_quit = Button(root, text="Exit Program", command=root.quit) # button to close a program

button_quit.pack()

root.mainloop()