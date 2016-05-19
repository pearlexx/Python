from tkinter import *

root = Tk()

photo = PhotoImage(file="thePhoto.jpg")
label = Label(root, image=photo)
label.pack()

root.mainloop()