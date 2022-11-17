from tkinter import *
from tkinter import StringVar


def magic() :
    Label(text="Hello User! Have a Nice Day...", bg="white", anchor="center", relief=SUNKEN).pack(fill=Y, pady=40)

root = Tk()
root.title("Hello World in GUI - Pycharm")
root.geometry("700x300")

Label(text = "Hello World!" , bg= "yellow", anchor= "center", relief= SUNKEN).pack(fill = Y, pady = 40)
Button(text = "Click Me", command = magic).pack()


root.mainloop()
