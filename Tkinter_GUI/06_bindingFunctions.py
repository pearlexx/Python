from tkinter import *

root = Tk()

# Method 1
"""

def printName():
    print("Hello, my name is Cyrus!")

button_1 = Button(root, text="Print the Name", command=printName)
button_1.pack()

"""

# Method 2 (better method)
def printName(event):
    print("Hello, my name is Cyrus!")

button_1 = Button(root, text="Print the Name")
button_1.bind("<Button-1>", printName)
button_1.pack()

root.mainloop()