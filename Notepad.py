from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os

def newFile():
    global file
    root.title("Untitled - Notepad")
    file = None
    TextArea.delete(1.0, END) #1.0 = 1st line, 0 th chr



def openFile():
    global file
    file = asksaveasfilename(defaultextension= ".txt",
                           filetypes=[("ALl Files", "*.*"),
                                      ("Text Documents", "*.txt")])

    if file == "":
        file = None
    else :
        root.title(os.path.basename(file) + "- Notepad")
        TextArea.delete(1.0, END)
        f = open(file, "r")
        TextArea.insert(1.0, f.read())
        f.close()

def saveFile():
    global file
    if file == None:
        file = asksaveasfilename(initialfile= 'Untitled.txt',defaultextension= ".txt",
                           filetypes=[("ALl Files", "*.*"),
                                      ("Text Documents", "*.txt")])
        if file == "" :
            file = None
        else :
            #Save as a new file
            f = open(file, "w")
            f.write(TextArea.get(1.0, END))
            f.close()

            root.title(os.path.basename(file)+ " - Notepad")
            print("File Saved")
    else :
        #Save The file
        f = open(file, "w")
        f.write(TextArea.get(1.0, END))
        f.close()




def quitApp():
    root.destroy()

def cut():
    TextArea.event_generate("<<Cut>>")

def copy():
    TextArea.event_generate("<<Copy>>")

def paste():
    TextArea.event_generate("<<Paste>>")

def about():
    showinfo("Notepad", "Notepad by Sayan Ghosh")






if __name__ == '__main__':
    #Basic tkinter setup
    root = Tk()
    root.title("Untitled - Notepad")
    root.wm_iconbitmap("notepad.ico")
    root.geometry("700x400")


    #Add Textarea
    TextArea = Text(root, font = "calibri 12")
    file = None
    TextArea.pack(fill = "both", expand= True)

    #lets create a menubar
    Menubar = Menu(root)
    # File Menu starts
    FileMenu = Menu(Menubar, tearoff = 0)

    #to open new file
    FileMenu.add_command(label = "New", command = newFile)

    #to open and already existing file
    FileMenu.add_command(label = "Open", command= openFile)

    #to save the current file

    FileMenu.add_command(label = "Save", command= saveFile)
    FileMenu.add_separator()
    FileMenu.add_command(label= "Exit", command = quitApp)
    Menubar.add_cascade(label = "File", menu = FileMenu)
    # File Menu ends

    # Edit Menu starts
    EditMenu  = Menu(Menubar, tearoff= 0)

    #To give a feature of cut, copy and paste
    EditMenu.add_command(label = "Cut", command = cut)
    EditMenu.add_command(label="Copy", command=copy)
    EditMenu.add_command(label="Paste", command=paste)

    Menubar.add_cascade(label = "Edit", menu = EditMenu)
    # Edit Menu ends

    # Help Menu starts

    HelpMenu = Menu(Menubar, tearoff = 0)
    HelpMenu.add_command(label = "About Notepad", command = about)
    Menubar.add_cascade(label="Help", menu=HelpMenu)




    root.config(menu = Menubar)

    #Adding scrollbar
    Scroll = Scrollbar(TextArea)
    Scroll.pack(side = RIGHT, fill= Y)
    Scroll.config(command = TextArea.yview)
    TextArea.config(yscrollcommand= Scroll.set)


root.mainloop()
