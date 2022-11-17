from tkinter import *

root = Tk()

root.geometry("400x300")
root.title("Slider Tutorial")

#For connecting scrollbar to a widget
# 1. widget(yscrollcommanf = scrollbar.set)
# 2. scrollbar.config(command = widget.yview)
scrollbar = Scrollbar(root)
scrollbar.pack(side = RIGHT, fill=Y)

'''listbox = Listbox(root)
for i in range(344) :
    listbox.insert(END, f"Item {i}")
listbox.pack(fill = "both", pady = 220, padx = 220)'''
text = Text(root, yscrollcommand= scrollbar.set)
text.pack(fill = "both")




scrollbar.config(command = text.yview)








root.mainloop()