import os
from tkinter import *
import tkinter.messagebox as msbox
from tkinter.filedialog import askopenfilename, asksaveasfilename


root = Tk()
root.title("Note It Up")


gui_width = 600
gui_height = 400
root.geometry(f"{gui_width}x{gui_height}")


def new_file(event=None):
    global current_file
    root.title("Untitled - Note It Up")
    current_file = None
    text_screen.delete(1.0, END)

def open_file(event=None):
    global current_file
    current_file = askopenfilename(defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
    
    if current_file == "":
        current_file = None
    else:
        root.title(os.path.basename(current_file)+" - Note It Up")
        text_screen.delete(1.0, END)
        f = open(current_file, "r")
        text_screen.insert(1.0, f.read())
        f.close()

def save_file(event=None):
    global current_file
    if current_file == None:
        current_file = asksaveasfilename(initialfile="Untitled.txt", defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])

        if current_file == "":
            current_file = None
        else:
            f = open(current_file, 'w')
            f.write(text_screen.get(1.0, END))
            f.close()
            root.title(os.path. basename(current_file)+" - Note It Up")

    else:             
        f = open(current_file, 'w')
        f.write(text_screen.get(1.0, END))
        f.close()

def quit_app():
    root.destroy()

def cut():
    text_screen.event_generate(("<<Cut>>"))

def copy():
    text_screen.event_generate(("<<Copy>>"))

def paste():
    text_screen.event_generate(("<<Paste>>"))

def about():
    msbox.showinfo("About Us!", "This is a basic notepad made by Ronit.\nWant to contact? Feel free to contact.\n→ ronitbhati.786@gmail.com")


text_screen = Text(root, font="lucida 13")
text_screen.pack(expand=TRUE, fill=BOTH)


scroll = Scrollbar(text_screen)
scroll.pack(side=RIGHT, fill=Y)


scroll.config(command=text_screen.yview)
text_screen.config(yscrollcommand=scroll.set)


current_file = None


menubar = Menu(root)

menu_file = Menu(menubar, tearoff=0)
menu_file.add_command(label="New", command=new_file)
menu_file.add_command(label="Open", command=open_file)
menu_file.add_command(label="Save", command=save_file)
menu_file.add_separator()
menu_file.add_command(label="Exit", command=quit_app)
menubar.add_cascade(label="File", menu=menu_file)


menu_edit = Menu(menubar, tearoff=0)
menu_edit.add_command(label="Cut", command=cut)
menu_edit.add_command(label="Copy", command=copy)
menu_edit.add_command(label="Paste", command=paste)
menubar.add_cascade(label="Edit", menu=menu_edit)


menu_help = Menu(menubar, tearoff=0)
menu_help.add_command(label="About", command=about)
menubar.add_cascade(label="Help", menu=menu_help)


root.bind('<Control-s>', save_file)
root.bind('<Control-o>', open_file)
root.bind('<Control-n>', new_file)


root.config(menu=menubar)


root.mainloop()