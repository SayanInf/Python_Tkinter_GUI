'''A Calculator Made by Sayan with the help of Code with Harry'''

from tkinter import *
from math import*
from tkinter.messagebox import showinfo

root = Tk()
root.geometry("700x700")
root.wm_iconbitmap("calculator.ico")
root.title("Sayan's Calculator")


def click(event):
    global scvalue
    text = event.widget.cget("text")

    if text == "=" :
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else :
            try:
                value = eval(scvalue.get())
            except Exception as e:
                scvalue.set(value = "Error")
                screen.update()

        scvalue.set(value)
        screen.update()

    elif text == "C" :
        scvalue.set("")
        screen.update()

    elif text == "←" :
        value = str(scvalue.get())
        value = list(value)
        value.pop(-1)
        k =""
        for i in value :
            k += i
        scvalue.set(k)
        screen.update()
        
        

    else :
        scvalue.set(scvalue.get()+text)
        screen.update()





def about():
    showinfo("Caluculator Instructions", '''Calculator by Sayan Ghosh :-\n\n1. pi, inf, tau are constants and their values are
3.1415..., 2.7182..., 6.2831..., respectively.
\n2. degrees, radians, factorial take inputs only and only in between parentheses["( )"]. For example: factorial(4) = 24
\n3. perm and comb are referred as nPr and nCr and take input as func_name(n,r). For example: perm(3,2) = 6.
\n4. fmod is referred as remainder when x is divided by y and the syntax is fmod(x,y). For example : fmod(3,2) = 1
\n5. All trigonometric and logarithmic functions take inputs only and only in between parentheses["( )"]. For example: sin(0) = 0
\n\nFor better ideas to improve the calculator and for errors and bug reports, kindly contact me on Telegram...
\n Telegram user id: @SayanGhosh121''')



Menubar = Menu(root)

# Help Menu starts

HelpMenu = Menu(Menubar, tearoff = 0)
HelpMenu.add_command(label = "About Calculator", command = about)
Menubar.add_cascade(label="Help", menu=HelpMenu)
root.config(menu = Menubar)


scvalue = StringVar()
scvalue.set("")
screen = Entry(root, text= scvalue, font= "luclida 35 bold")
screen.pack(fill = X, ipadx= 20,ipady = 8, padx = 10, pady = 10)


f = Frame(root, bg = "white")
b = Button(f, text= "pi",padx = 16, pady = 10, font = "lucida 15 bold")
b.pack(side= LEFT, padx = 5, pady= 5)
b.bind("<Button-1>", click)

b = Button(f, text= "inf",padx = 16, pady = 10, font = "lucida 15 bold")
b.pack(side= LEFT, padx = 5, pady= 5)
b.bind("<Button-1>", click)

b = Button(f, text= "tau",padx = 16, pady = 10, font = "lucida 15 bold")
b.pack(side= LEFT, padx = 5, pady= 5)
b.bind("<Button-1>", click)

b = Button(f, text= "degrees",padx = 1, pady = 10, font = "lucida 15 bold")
b.pack(side= LEFT, padx = 5, pady= 5)
b.bind("<Button-1>", click)

b = Button(f, text= "radians",padx = 1, pady = 10, font = "lucida 15 bold")
b.pack(side= LEFT, padx = 5, pady= 5)
b.bind("<Button-1>", click)

f.pack()

f = Frame(root, bg = "white")

b = Button(f, text= "factorial",padx = 15, pady = 10, font = "lucida 15 bold")
b.pack(side= LEFT, padx = 5, pady= 5)
b.bind("<Button-1>", click)

b = Button(f, text= "fmod",padx = 15, pady = 10, font = "lucida 15 bold")
b.pack(side= LEFT, padx = 5, pady= 5)
b.bind("<Button-1>", click)

b = Button(f, text= "perm",padx = 15, pady = 10, font = "lucida 15 bold")
b.pack(side= LEFT, padx = 5, pady= 5)
b.bind("<Button-1>", click)

b = Button(f, text= "comb",padx = 15, pady = 10, font = "lucida 15 bold")
b.pack(side= LEFT, padx = 5, pady= 5)
b.bind("<Button-1>", click)

f.pack()

f = Frame(root, bg = "white")
b = Button(f, text= "sin",padx = 14, pady = 10, font = "lucida 15 bold")
b.pack(side= LEFT, padx = 5, pady= 5)
b.bind("<Button-1>", click)

b = Button(f, text= "cos",padx = 14, pady = 10, font = "lucida 15 bold")
b.pack(side= LEFT, padx = 5, pady= 5)
b.bind("<Button-1>", click)

b = Button(f, text= "tan",padx = 14, pady = 10, font = "lucida 15 bold")
b.pack(side= LEFT, padx = 5, pady= 5)
b.bind("<Button-1>", click)

b = Button(f, text= "log10",padx = 16, pady = 10, font = "lucida 15 bold")
b.pack(side= LEFT, padx = 5, pady= 5)
b.bind("<Button-1>", click)

b = Button(f, text= "log",padx = 17, pady = 10, font = "lucida 15 bold")
b.pack(side= LEFT, padx = 5, pady= 5)
b.bind("<Button-1>", click)

f.pack()

f = Frame(root, bg = "white")
b = Button(f, text= "asin",padx = 11, pady = 10, font = "lucida 10 bold")
b.pack(side= LEFT, padx = 5, pady= 5)
b.bind("<Button-1>", click)

b = Button(f, text= "acos",padx = 11, pady = 10, font = "lucida 10 bold")
b.pack(side= LEFT, padx = 5, pady= 5)
b.bind("<Button-1>", click)

b = Button(f, text= "atan",padx = 11, pady = 10, font = "lucida 10 bold")
b.pack(side= LEFT, padx = 5, pady= 5)
b.bind("<Button-1>", click)

b = Button(f, text= "asinh",padx = 13, pady = 10, font = "lucida 10 bold")
b.pack(side= LEFT, padx = 5, pady= 5)
b.bind("<Button-1>", click)

b = Button(f, text= "acosh",padx = 13, pady = 10, font = "lucida 10 bold")
b.pack(side= LEFT, padx = 5, pady= 5)
b.bind("<Button-1>", click)

b = Button(f, text= "atanh",padx = 13, pady = 10, font = "lucida 10 bold")
b.pack(side= LEFT, padx = 5, pady= 5)
b.bind("<Button-1>", click)

f.pack()


f = Frame(root, bg = "white")
b = Button(f, text= "7",padx = 20, pady = 10, font = "lucida 20 bold")
b.pack(side= LEFT, padx = 5, pady= 5)
b.bind("<Button-1>", click)

b = Button(f, text= "8",padx = 20, pady = 10, font = "lucida 20 bold")
b.pack(side= LEFT, padx = 5, pady= 5)
b.bind("<Button-1>", click)

b = Button(f, text= "9",padx = 20, pady = 10, font = "lucida 20 bold")
b.pack(side= LEFT, padx = 5, pady= 5)
b.bind("<Button-1>", click)

b = Button(f, text= "C",padx = 19, pady = 10, font = "lucida 20 bold")
b.pack(side= LEFT, padx = 5, pady= 5)
b.bind("<Button-1>", click)

b = Button(f, text= "←",padx = 16, pady = 10, font = "lucida 20 bold")
b.pack(side= LEFT, padx = 5, pady= 5)
b.bind("<Button-1>", click)

f.pack()

f = Frame(root, bg = "white")
b = Button(f, text= "4",padx = 20, pady = 10, font = "lucida 20 bold")
b.pack(side= LEFT, padx = 5, pady= 5)
b.bind("<Button-1>", click)

b = Button(f, text= "5",padx = 20, pady = 10, font = "lucida 20 bold")
b.pack(side= LEFT, padx = 5, pady= 5)
b.bind("<Button-1>", click)

b = Button(f, text= "6",padx = 20, pady = 10, font = "lucida 20 bold")
b.pack(side= LEFT, padx = 5, pady= 5)
b.bind("<Button-1>", click)

b = Button(f, text= "*",padx = 25, pady = 10, font = "lucida 20 bold")
b.pack(side= LEFT, padx = 5, pady= 5)
b.bind("<Button-1>", click)

b = Button(f, text= "/",padx = 24, pady = 10, font = "lucida 20 bold")
b.pack(side= LEFT, padx = 5, pady= 5)
b.bind("<Button-1>", click)

f.pack()

f = Frame(root, bg = "white")
b = Button(f, text= "1",padx = 20, pady = 10, font = "lucida 20 bold")
b.pack(side= LEFT, padx = 5, pady= 5)
b.bind("<Button-1>", click)

b = Button(f, text= "2",padx = 20, pady = 10, font = "lucida 20 bold")
b.pack(side= LEFT, padx = 5, pady= 5)
b.bind("<Button-1>", click)

b = Button(f, text= "3",padx = 20, pady = 10, font = "lucida 20 bold")
b.pack(side= LEFT, padx = 5, pady= 5)
b.bind("<Button-1>", click)

b = Button(f, text= "+",padx = 23, pady = 10, font = "lucida 20 bold")
b.pack(side= LEFT, padx = 5, pady= 5)
b.bind("<Button-1>", click)

b = Button(f, text= "-",padx = 23, pady = 10, font = "lucida 20 bold")
b.pack(side= LEFT, padx = 5, pady= 5)
b.bind("<Button-1>", click)

f.pack()

f = Frame(root, bg = "white")
b = Button(f, text= "0",padx = 20, pady = 10, font = "lucida 20 bold")
b.pack(side= LEFT, padx = 5, pady= 5)
b.bind("<Button-1>", click)

b = Button(f, text= ".",padx = 5, pady = 10, font = "lucida 20 bold")
b.pack(side= LEFT, padx = 2, pady= 5)
b.bind("<Button-1>", click)

b = Button(f, text= ",",padx = 5, pady = 10, font = "lucida 20 bold")
b.pack(side= LEFT, padx = 2, pady= 5)
b.bind("<Button-1>", click)

b = Button(f, text= "(",padx = 23, pady = 10, font = "lucida 20 bold")
b.pack(side= LEFT, padx = 5, pady= 5)
b.bind("<Button-1>", click)

b = Button(f, text= ")",padx = 23, pady = 10, font = "lucida 20 bold")
b.pack(side= LEFT, padx = 5, pady= 5)
b.bind("<Button-1>", click)

b = Button(f, text= "=",padx = 22, pady = 10, font = "lucida 20 bold")
b.pack(side= LEFT, padx = 5, pady= 5)
b.bind("<Button-1>", click)

f.pack()




root.mainloop()
