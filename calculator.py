from tkinter import *
from math import *

root=Tk()            #ROOT WIDGET
root.title(" Jaskirat's Personal Scientific Calculator")

e = Entry(root, width=35, borderwidth=4)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

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

def button_equal():
    second_number = e.get()
    e.delete(0, END)
    
    if math == "addition":
        e.insert(0, f_num + int(second_number))
        
    if math == "subtraction":
        e.insert(0, f_num - int(second_number))
        
    if math == "multiplication":
        e.insert(0, f_num * int(second_number))
        
    if math == "division":
        e.insert(0, f_num / int(second_number))

    if math == "square":
        e.insert(0, f_num ** 2)

    if math == "squareroot":
        e.insert(0, sqrt(f_num))
        
    if math == "exponential":
        e.insert(0, exp(f_num))
        
    if math == "naturallogarithm":
        e.insert(0, log(f_num))
        
    if math == "logarithm":
        e.insert(0, log10(f_num))
        
    if math == "facto":
        e.insert(0, factorial(f_num))
        
    if math == "sine":
        e.insert(0, sin(f_num))
        
    if math == "cosine":
        e.insert(0, cos(f_num))

    if math == "tangent":
        e.insert(0, tan(f_num))
        
    if math == "powerr":
        e.insert(0, (f_num) ** int(second_number))
        
def button_subtract():
    first_number = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_number)
    e.delete(0, END)
    
def button_multiply():
    first_number = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_number)
    e.delete(0, END)
    
def button_divide():
    first_number = e.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_number)
    e.delete(0, END)
    
def button_square():
    first_number = e.get()
    global f_num
    global math
    math = "square"
    f_num = int(first_number)
    e.delete(0, END)
    
def button_squareroot():
    first_number = e.get()
    global f_num
    global math
    math = "squareroot"
    f_num = int(first_number)
    e.delete(0, END)
    
def button_exponential():
    first_number = e.get()
    global f_num
    global math
    math = "exponential"
    f_num = int(first_number)
    e.delete(0, END)
    
def button_naturallogarithm():
    first_number = e.get()
    global f_num
    global math
    math = "naturallogarithm"
    f_num = int(first_number)
    e.delete(0, END)
    
def button_logarithm():
    first_number = e.get()
    global f_num
    global math
    math = "logarithm"
    f_num = int(first_number)
    e.delete(0, END)
    
def button_facto():
    first_number = e.get()
    global f_num
    global math
    math = "facto"
    f_num = int(first_number)
    e.delete(0, END)
    
def button_sine():
    first_number = e.get()
    global f_num
    global math
    math = "sine"
    f_num = int(first_number)
    e.delete(0, END)

def button_cosine():
    first_number = e.get()
    global f_num
    global math
    math = "cosine"
    f_num = int(first_number)
    e.delete(0, END)
    
def button_tangent():
    first_number = e.get()
    global f_num
    global math
    math = "tangent"
    f_num = int(first_number)
    e.delete(0, END)
    
def button_powerr():
    first_number = e.get()
    global f_num
    global math
    math = "powerr"
    f_num = int(first_number)
    e.delete(0, END)
    
    
#DEFINE BUTTONS

button_1 = Button(root, text="1", padx=40, pady=20, command= lambda: button_click(1))
button_2 = Button(root, text="2", padx=40, pady=20, command= lambda: button_click(2))
button_3 = Button(root, text="3", padx=40, pady=20, command= lambda: button_click(3))
button_4 = Button(root, text="4", padx=40, pady=20, command= lambda: button_click(4))
button_5 = Button(root, text="5", padx=40, pady=20, command= lambda: button_click(5))
button_6 = Button(root, text="6", padx=40, pady=20, command= lambda: button_click(6))
button_7 = Button(root, text="7", padx=40, pady=20, command= lambda: button_click(7))
button_8 = Button(root, text="8", padx=40, pady=20, command= lambda: button_click(8))
button_9 = Button(root, text="9", padx=40, pady=20, command= lambda: button_click(9))
button_0 = Button(root, text="0", padx=40, pady=20, command= lambda: button_click(0))

button_add = Button(root, text="+", padx=39, pady=20, command=button_add)
button_equal = Button(root, text="=", padx=89, pady=20, command=button_equal)
button_clear = Button(root, text="Clear", padx=79, pady=20, command=button_clear)
button_subtract = Button(root, text="-", padx=41, pady=20, command=button_subtract)
button_multiply = Button(root, text="×", padx=41, pady=20, command=button_multiply)
button_divide = Button(root, text="/", padx=41, pady=20, command=button_divide)
button_square = Button(root, text="x²", padx=38, pady=20, command=button_square)
button_squareroot = Button(root, text="√x", padx=38, pady=20, command=button_squareroot)
button_exponential = Button(root, text="e^x", padx=34, pady=20, command=button_exponential)
button_naturallogarithm = Button(root, text="ln", padx=37, pady=20, command=button_naturallogarithm)
button_logarithm = Button(root, text="log10", padx=28, pady=20, command=button_logarithm)
button_facto = Button(root, text="n!", padx=37, pady=20, command=button_facto)
button_sine = Button(root, text="sin", padx=35, pady=20, command=button_sine)
button_cosine = Button(root, text="cos", padx=34, pady=20, command=button_cosine)
button_tangent = Button(root, text="tan", padx=34, pady=20, command=button_tangent)
button_powerr = Button(root, text="^", padx=38, pady=20, command=button_powerr)



#PUTTING THE BUTTONS ON THE SCREEN


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
button_clear.grid(row=4, column=1, columnspan=2)

button_add.grid(row=5, column=0)
button_equal.grid(row=5, column=1, columnspan=2)

button_subtract.grid(row=6, column=0)
button_multiply.grid(row=6, column=1)
button_divide.grid(row=6, column=2)

button_square.grid(row=7, column=0)
button_squareroot.grid(row=7, column=1)
button_exponential.grid(row=7, column=2)

button_naturallogarithm.grid(row=1, column=3)
button_logarithm.grid(row=2, column=3)
button_facto.grid(row=3, column=3)
button_sine.grid(row=4, column=3)
button_cosine.grid(row=5, column=3)
button_tangent.grid(row=6, column=3)
button_powerr.grid(row=7, column=3)





root.mainloop()