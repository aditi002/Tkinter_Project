from tkinter import *
root = Tk()
def myClick():
    myLabel = Label(root,text="BUTTON IS CLICKED!!",fg="white",bg="black")
    myLabel.pack()

myButton = Button(root, text="CLICK ME!",fg="white",bg="black", command= myClick)
myButton.pack()
root.mainloop()