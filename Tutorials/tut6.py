from tkinter import *

root = Tk()

root.geometry("700x600")
root.title("My First GUI With Harry")

'''Important Label Options
text = adds the text
bg = background
fg = forefround
font = sets the font
1. font= ("comicsansms", 12, "bold")
2. font= (comicsansms 12 bold)
padx = x padding
pady = y padding
relief = border styling - SUNKEN, RAISED, GROOVE, RIDGE'''

title_label = Label(text = '''Science is a systematic enterprise that builds and organizes knowledge in 
the form of testable explanations and predictions about the universe.
The earliest roots in the history of science can be traced to Ancient
Egypt and Mesopotamia in around 3000 to 1200 BCE.[3][4] Their contributions to mathematics, 
astronomy, and medicine entered and shaped Greek natural
nphilosophy of classical antiquity, whereby formal attempts were made to prov
\ide explanations of events in the physical world based on natural causes.[3][4] After the fa
\ll of the Western Roman Empire, knowledge of Greek conceptions of the world deteriorated in Western
\Europe during the early centuries (400 to 1000 CE) of the Middle Ages,[5] but was preserved in the Muslim
\world during the Islamic Golden Age.[6]''', bg = "red", padx = 23, pady = 44, font= ("comicsansms", 12, "bold"), borderwidth= 5, relief = SUNKEN )


'''Important pack options
anchor = nw
side = TOP, BOTTOM, LEFT, RiGHT
fill 
'''

title_label.pack(anchor = "center", side = TOP, fill=Y, pady= 100)

root.mainloop()