import math
from _ast import Lambda
from tkinter import *
from tkinter.font import Font
from tkinter import messagebox
root = Tk()
root.title("Simple Calculator")
root.configure(background='black')
root.iconbitmap('C:/Users/ACER/Desktop/calc.ico')
fontStyle = Font(family="Lucida Grande", size=30)


e = Entry(root, width = 50, borderwidth =20, fg='#00FFFF', bg='black',font="fontStyle")
e.grid(row=0, column=0, columnspan=6, padx=40, pady=20)

font_tuple = ("Georgia", 20)

def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def button_clear():
    e.delete(0, END)

def button_add():
    first_number = e.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    e.delete(0, END)

def button_sub():
    first_number = e.get()
    global f_num
    global math
    math = "substraction"
    f_num = int(first_number)
    e.delete(0, END)

def button_mul():
    first_number = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_number)
    e.delete(0, END)

def button_div():
    first_number = e.get()

    global f_num
    global math
    math = "division"
    f_num = int(first_number)
    e.delete(0, END)


def button_mod():
    first_number = e.get()
    global f_num
    global math
    math = "modulus"
    f_num = int(first_number)
    e.delete(0, END)


def button_equal():
    second_number = e.get()
    e.delete(0,END)
    if math =="addition":
        e.insert(0, f_num + int(second_number))
    if math =="substraction":
        e.insert(0, f_num - int(second_number))
    if math =="multiplication":
        e.insert(0, f_num * int(second_number))
    if math == "division":
        try:
            e.insert(0, f_num / int(second_number))
        except ZeroDivisionError:
            messagebox.showerror("Error!!", "A number can't be divided by zero.")

    if math =="modulus":
        e.insert(0, f_num % int(second_number))


def button_erase():
    length = len(e.get())
    e.delete(length - 1, 'end')
    if length == 1:
        e.insert(0, "")


button_1 = Button(root, text="1",padx=52,pady=20,bg="black", fg="#66ff00", font=font_tuple, command=lambda:button_click(1))
button_1.grid(row=3,column=0)
button_2 = Button(root, text="2",padx=50,pady=20,bg="black", fg="#66ff00", font=font_tuple, command=lambda:button_click(2))
button_2.grid(row=3,column=1)
button_3 = Button(root, text="3",padx=50,pady=20,bg="black", fg="#66ff00", font=font_tuple, command=lambda:button_click(3))
button_3.grid(row=3,column=2)
button_4 = Button(root, text="4",padx=50,pady=20,bg="black", fg="#66ff00", font=font_tuple, command=lambda:button_click(4))
button_4.grid(row=2,column=0)
button_5 = Button(root, text="5",padx=50,pady=20,bg="black", fg="#66ff00", font=font_tuple, command=lambda:button_click(5))
button_5.grid(row=2,column=1)
button_6 = Button(root, text="6",padx=50,pady=20,bg="black", fg="#66ff00", font=font_tuple, command=lambda:button_click(6))
button_6.grid(row=2,column=2)
button_7 = Button(root, text="7",padx=50,pady=20,bg="black", fg="#66ff00", font=font_tuple, command=lambda:button_click(7))
button_7.grid(row=1,column=0)
button_8 = Button(root, text="8",padx=50,pady=20,bg="black", fg="#66ff00", font=font_tuple, command=lambda:button_click(8))
button_8.grid(row=1,column=1)
button_9 = Button(root, text="9",padx=50,pady=20,bg="black", fg="#66ff00", font=font_tuple, command=lambda:button_click(9))
button_9.grid(row=1,column=2)
button_0 = Button(root, text="0",padx=50,pady=20,bg="black", fg="#66ff00", font=font_tuple, command=lambda:button_click(0))
button_0.grid(row=4,column=0)


button_add = Button(root, text="+",padx=61,pady=20,fg="#BF40BF", bg="black", font=font_tuple, command=button_add)
button_add.grid(row=2,column=3)
button_sub = Button(root, text="-",padx=64,pady=20,fg="#BF40BF", bg="black", font=font_tuple, command=button_sub)
button_sub.grid(row=3,column=3)
button_mul = Button(root, text="*",padx=67,pady=20,fg="#BF40BF", bg="black", font=font_tuple, command=button_mul)
button_mul.grid(row=2,column=4)
button_div= Button(root, text="÷",padx=67,pady=20,fg="#BF40BF", bg="black", font=font_tuple, command=button_div)
button_div.grid(row=3,column=4)
button_mod= Button(root, text="mod",padx=42,pady=20,fg="#BF40BF", bg="black", font=font_tuple, command=button_mod)
button_mod.grid(row=4,column=3)


button_equal = Button(root, text="=",padx=65,pady=20,fg="#FFFF00", bg="black", font=font_tuple, command=button_equal)
button_equal.grid(row=4,column=4)
button_clear= Button(root, text="CLEAR",padx=84,pady=20,fg="#FFFF00", bg="black", font=font_tuple, command=button_clear)
button_clear.grid(row=4,column=1,columnspan=2)
button_erase= Button(root, text="⇦",padx=143,pady=20,fg="#FFFF00", bg="black", font=font_tuple, command=button_erase)
button_erase.grid(row=1,column=3,columnspan=2)

root.mainloop()

