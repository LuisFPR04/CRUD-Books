from tkinter import * 
from CRUDbooktable import crud

root2 = Tk()
root2.title("Librería Pepe")

crudbutton = Button(root2, text="Book table", command=crud).grid(column=0,row=0)

root2.mainloop()