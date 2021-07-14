from tkinter import *
from PIL import ImageTk, Image
root = Tk()
root.title('Images Insertion')
root.iconbitmap('C:/Users/ACER/Desktop/cal.ico')
my_image = ImageTk.PhotoImage(Image.open('C:/Users/ACER/Desktop/image.jpg'))
my_label = Label(image= my_image)
my_label.pack()
button_quit = Button(root, text="Exit",command=root.quit,width=20)
button_quit.pack()
root.mainloop()



