from tkinter import *

root=Tk()
root.title("Simple Calculator")
e=Entry(root, width=35, borderwidth=5, bg="yellow")
e.grid(row=0, column=0, columnspan=3, padx=10,pady=10)

def add(number):
    
    x=e.get()
    e.delete(0, END)
    e.insert(0, str(x)+str(number))

def clear():
    e.delete(0,END)

def addition():
    first=e.get()
    global f_num
    global math
    math="adding"
    f_num=int(first)
    e.delete(0,END)

def equal():
    second=e.get()
    e.delete(0,END)

    if math=="adding":
        e.insert(0, f_num + int(second))
    if math=="subtract":
        e.insert(0, f_num - int(second))
    if math=="multiply":
        e.insert(0, f_num * int(second))
    if math=="divide":
        e.insert(0, f_num / int(second))

def sub():
    first=e.get()
    global f_num
    global math
    math="subtract"
    f_num=int(first)
    e.delete(0,END)

def  mul():
    first=e.get()
    global f_num
    global math
    math="multiply"
    f_num=int(first)
    e.delete(0,END)

def div():
    first=e.get()
    global f_num
    global math
    math="divide"
    f_num=int(first)
    e.delete(0,END)


#def button

button_1=Button(root, text="1", padx=40, pady=20, command=lambda: add(1) ,bg="yellow")
button_2=Button(root, text="2", padx=40, pady=20, command=lambda: add(2),bg="yellow")
button_3=Button(root, text="3", padx=40, pady=20, command=lambda: add(3),bg="yellow")
button_4=Button(root, text="4", padx=40, pady=20, command=lambda: add(4),bg="yellow")
button_5=Button(root, text="5", padx=40, pady=20, command=lambda: add(5),bg="yellow")
button_6=Button(root, text="6", padx=40, pady=20, command=lambda: add(6),bg="yellow")
button_7=Button(root, text="7", padx=40, pady=20, command=lambda: add(7),bg="yellow")
button_8=Button(root, text="8", padx=40, pady=20, command=lambda: add(8),bg="yellow")
button_9=Button(root, text="9", padx=40, pady=20, command=lambda: add(9),bg="yellow")
button_0=Button(root, text="0", padx=40, pady=20, command=lambda: add(0),bg="yellow")
button_add=Button(root, text="+", padx=39, pady=20, command=lambda: addition(),bg="yellow")
button_equal=Button(root, text="=", padx=88, pady=20, command=lambda: equal(),bg="yellow")
button_clear=Button(root, text="Clear", padx=78, pady=20, command=lambda: clear(),bg="yellow")

button_sub=Button(root, text="-", padx=40, pady=20, command=lambda: sub(),bg="yellow")
button_mul=Button(root, text="*", padx=40, pady=20, command=lambda: mul(),bg="yellow")
button_div=Button(root, text="/", padx=40, pady=20, command=lambda: div(),bg="yellow")
#create button

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)

button_add.grid(row=5, column=0,)
button_clear.grid(row=4, column=1,columnspan=2)
button_equal.grid(row=5, column=1,columnspan=2)

button_sub.grid(row=6, column=0)
button_mul.grid(row=6, column=1)
button_div.grid(row=6, column=2)

root.mainloop()