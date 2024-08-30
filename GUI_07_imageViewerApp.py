from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('image viewer App')

root.iconbitmap('E:/HTML & CSS/icons/crown.ico') # icon at the start of a title

my_img1 = ImageTk.PhotoImage(Image.open("E:/HTML & CSS/thumbnails/thumbnail-1.webp"))
my_img2 = ImageTk.PhotoImage(Image.open("E:/HTML & CSS/thumbnails/thumbnail-2.webp"))
my_img3 = ImageTk.PhotoImage(Image.open("E:/HTML & CSS/thumbnails/thumbnail-3.webp"))
my_img4 = ImageTk.PhotoImage(Image.open("E:/HTML & CSS/thumbnails/thumbnail-4.webp"))
my_img5 = ImageTk.PhotoImage(Image.open("E:/HTML & CSS/thumbnails/thumbnail-5.webp"))
my_img6 = ImageTk.PhotoImage(Image.open("E:/HTML & CSS/thumbnails/thumbnail-6.webp"))
my_img7 = ImageTk.PhotoImage(Image.open("E:/HTML & CSS/thumbnails/thumbnail-7.webp"))
my_img8 = ImageTk.PhotoImage(Image.open("E:/HTML & CSS/thumbnails/thumbnail-8.webp"))
my_img9 = ImageTk.PhotoImage(Image.open("E:/HTML & CSS/thumbnails/thumbnail-9.webp"))
my_img10 = ImageTk.PhotoImage(Image.open("E:/HTML & CSS/thumbnails/thumbnail-10.webp"))
my_img11 = ImageTk.PhotoImage(Image.open("E:/HTML & CSS/thumbnails/thumbnail-11.webp"))
my_img12 = ImageTk.PhotoImage(Image.open("E:/HTML & CSS/thumbnails/thumbnail-12.webp"))

image_list = [my_img1, my_img2, my_img3, my_img4, my_img5, my_img6, my_img7, my_img8, my_img9, my_img10, my_img11, my_img12]



my_label = Label(image = my_img1)
my_label.grid(row=0, column=0, columnspan=3)


root.mainloop()