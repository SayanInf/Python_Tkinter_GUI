from tkinter import *

root = Tk()
root.geometry("700x600")

def getvals() :
    print(f"The value of username is {uservalue.get()}")
    print(f"The value of password is {passvalue.get()}")

user = Label(root, text = "Username")
password = Label(root, text = "Password")
user.grid()
password.grid(row= 1)

'''variable calsses in tkinter
BooleanVar, DoubleVar, IntVar, StringVar'''

uservalue = StringVar()
passvalue = StringVar()

userentry = Entry(root, textvariable= uservalue)
passentry = Entry(root, textvariable= passvalue)

userentry.grid(row = 0, column = 1)
passentry.grid(row = 1, column = 1)

Button(text = "Submit", command = getvals).grid()



root.mainloop()