from tkinter import *

a_root = Tk()

# GUI logic

# WidthxHeight
a_root.geometry("644x460")

# width, height
a_root.minsize(200,100)
a_root.maxsize(1200,988)

b = Label(text = "Hi It's my first GUI")
b.pack()


a_root.mainloop()
