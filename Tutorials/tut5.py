from tkinter import *
'''from PIL import Image, ImageTk'''

a_root = Tk()

a_root.geometry("900x800")
# For .png images
photo = PhotoImage(file = "Profile.png")

''''# For .jpg images
image = Image.open("JPG.jpg")
photo = ImageTk.PhotoImage(image)'''

b_label = Label(image = photo)
b_label.pack()


a_root.mainloop()