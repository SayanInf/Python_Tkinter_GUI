from tkinter import *
import tkinter.messagebox as tmsg

root = Tk()
root.geometry("400x300")
root.title("Radio Button Tutorial")

def order():
    tmsg.showinfo(title="Order Recieved", message=f"We have recieved {var.get()} as your order")

#var = IntVar()
var = StringVar()
var.set("Radio")
Label(root, text= "What would you like to have sir?", font = "lucida 19 bold",
      justify = LEFT, padx= 14).pack()
radio = Radiobutton(root, text = "Dosa", padx= 14, variable = var, value = "Dosa").pack(anchor= "w")
Radiobutton(root, text = "Idli", padx= 14, variable = var, value = "Idli").pack(anchor= "w")
Radiobutton(root, text = "Samosa", padx= 14, variable = var, value = "Samosa").pack(anchor= "w")

Button(text = "Order Now", command= order ).pack()

root.mainloop()