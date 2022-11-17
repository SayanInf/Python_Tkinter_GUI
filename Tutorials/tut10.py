from tkinter import *

root = Tk()
root.geometry("700x600")

def getvals() :
    print("It works")

#Heading
Label(root, text = "Welcome to Sayan's Travels",  font = "comicsansms 13 bold").grid(row = 0, column= 5)

#Texts for forms
name = Label(root, text = "Name")
phone = Label(root, text = "Phone")
gender = Label(root, text = "Gender")
emergency = Label(root, text = "Emergency Contact")
paymentmode = Label(root, text = "Payment Mode")

#Packing of names
name.grid(row = 1  , column = 2)
phone.grid(row = 2, column = 2)
gender.grid(row = 3, column = 2)
emergency.grid(row = 4, column = 2)
paymentmode.grid(row = 5, column = 2)

#Tkinter variables for storing entries
namevalue = StringVar()
phonevalue = StringVar()
gendervalue = StringVar()
emergencyvalue = StringVar()
paymentmodevalue = StringVar()
foodservicevalue = IntVar()

#Entries for a form
nameentry = Entry(root, textvariable = namevalue)
phoneentry = Entry(root, textvariable = phonevalue)
genderentry = Entry(root, textvariable = gendervalue)
emergencyentry = Entry(root, textvariable = emergencyvalue)
paymentmodeentry = Entry(root, textvariable = paymentmodevalue)

#Packing the entries
nameentry.grid(row = 1, column = 3)
phoneentry.grid(row = 2, column = 3)
genderentry.grid(row = 3, column = 3)
emergencyentry.grid(row = 4, column = 3)
paymentmodeentry.grid(row = 5, column = 3)

#Checkbox and packing it
foodservice = Checkbutton(text = "Want to prebook your meals", variable = foodservicevalue)
foodservice.grid(row = 6, column= 3)

#Button and packing it and assigning it a command
Button(text = "Submit", command = getvals).grid(row = 8, column= 3)


root.mainloop()