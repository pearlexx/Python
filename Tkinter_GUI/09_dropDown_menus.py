from tkinter import *


def doNothing():
    print("ok ok I won't...")

root = Tk()

menu1 = Menu(root)
root.config(menu=menu1)

subMenu = Menu(menu1)
menu1.add_cascade(label="File", menu=subMenu)
subMenu.add_command(label="New Project...", command=doNothing)
subMenu.add_command(label="New...", command=doNothing)
subMenu.add_separator()
subMenu.add_command(label="Exit", command=doNothing)

editMenu = Menu(menu1)
menu1.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Redo", command=doNothing)


root.mainloop()