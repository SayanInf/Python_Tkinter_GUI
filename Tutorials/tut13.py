from tkinter import *

def harry(event) :
    print(f"you clicked on the button at {event.x}, {event.y}")


root = Tk()
root.title("Events in Tkinter")
root.geometry("800x600")

widget = Button(root, text = "Click me Please")
widget.pack()

widget.bind('<Button-1>', harry)
widget.bind('<Double-1>', quit)


root.mainloop()