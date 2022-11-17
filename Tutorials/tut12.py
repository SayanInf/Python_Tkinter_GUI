from tkinter import *

root = Tk()

canvas_width = 800
canvas_height = 400

root.geometry(f"{canvas_width}x{canvas_height}")
can_widget = Canvas(root, width = canvas_width, height= canvas_height)
can_widget.pack()

# The line goes from the point x1, y1 to x2, y2
can_widget.create_line(0, 0, 800, 400, fill = "red")
can_widget.create_line(0, 400, 800, 0, fill = "blue")

# TO create a recangle specify paramater in this order - coords of top left
# and coords of bottom right
#can_widget.create_rectangle(0, 0, 400, 200, fill = "red")

# Coord of centre
can_widget.create_text(200,200, text ="Sayan")

# Coord of rectangle in which the oval would be fixed
can_widget.create_oval(5,9, 200,200)

root.mainloop()