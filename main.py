from tkinter import * 
from CRUDbooktable import crud

root = Tk()
root.title("Librería Pepe")

crudbutton = Button(root, text="Book table", command=crud).grid(column=0,row=0)

root.mainloop()