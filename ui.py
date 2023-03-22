from tkinter import *
from sqlite_com import ReadBooks, AddBooks

root = Tk()

def MyClick():
    myLabel = Label(root, text=ReadBooks)
    myLabel.pack

myButton = Button(root, text="Click", command=ReadBooks)
myButton.pack()
root.mainloop()