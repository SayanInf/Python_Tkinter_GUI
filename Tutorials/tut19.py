from tkinter import *
import tkinter.messagebox as tmsg

root = Tk()

root.geometry("400x300")
root.title("Slider Tutorial")

def getdollar():
    print(f"We have credited {myslider2.get()} dollars to your bank")
    tmsg.showinfo(title = "Amount Credited", message= f"We have credited {myslider2.get()} dollars to your bank")
#myslider1 = Scale(root, from_ = 0 , to = 455)
#myslider1.pack()

Label(root, text = "How many dollars do you want?").pack()

myslider2 = Scale(root, from_= 0 , to = 100, orient = HORIZONTAL, tickinterval= 50)
myslider2.set(50)
myslider2.pack()

Button(root, text = "Get Dollars", command= getdollar).pack()




root.mainloop()