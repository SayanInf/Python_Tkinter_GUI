from tkinter import *

root = Tk()
root.geometry("700x600")

def hello() :
    print("Hello World")
def name() :
    print("Sayan")

frame = Frame(root, border = 6, bg= "grey", relief = SUNKEN)
frame.pack(side = LEFT, anchor = "nw")

b1 = Button(frame, fg = "red", text = "Print Now", command = hello)
b1.pack(side= LEFT, padx = 20)

b2 = Button(frame, fg = "red", text = "Name", command = name)
b2.pack(side=LEFT, padx = 20)

b3 = Button(frame, fg = "red", text = "Print Now")
b3.pack(side= LEFT, padx = 20)

b4 = Button(frame, fg = "red", text = "Print Now")
b4.pack(side= LEFT, padx = 20)



root.mainloop()