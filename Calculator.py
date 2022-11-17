'''A Calculator Made by Sayan with the help of Code with Harry'''

from tkinter import *

root = Tk()
root.geometry("700x500")
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




scvalue = StringVar()
scvalue.set("")
screen = Entry(root, text= scvalue, font= "luclida 35 bold")
screen.pack(fill = X, ipadx= 20,ipady = 8, padx = 10, pady = 10)


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

b = Button(f, text= ".",padx = 24, pady = 10, font = "lucida 20 bold")
b.pack(side= LEFT, padx = 5, pady= 5)
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
