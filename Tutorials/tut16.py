from tkinter import *

root = Tk()

def myfunc():
    print("Hi")


root.geometry("733x566")
root.title("Sayan")

# Use this to create a non dropdown menu
#mymenu = Menu(root)
#mymenu.add_command(label= "File", command = myfunc)
#mymenu.add_command(label= "Exit", command = quit)
#root.config(menu = mymenu)

yourmenubar = Menu(root)
m1 = Menu(yourmenubar, tearoff = 0)
m1.add_command(label = "New Project", command = myfunc)
m1.add_command(label = "Save", command = myfunc)
m1.add_command(label = "Save As", command = myfunc)
m1.add_command(label = "Print", command = myfunc)
m1.add_command(label = "Quit", command = myfunc)
root.config(menu = yourmenubar)

yourmenubar.add_cascade(label = "File", menu = m1)

m2 = Menu(yourmenubar, tearoff = 0)
m2.add_command(label = "cut", command = myfunc)
m2.add_command(label = "copy", command = myfunc)
m2.add_command(label = "paste", command = myfunc)
m2.add_command(label = "find", command = myfunc)
root.config(menu = yourmenubar)

yourmenubar.add_cascade(label = "Edit", menu = m2)
root.mainloop()