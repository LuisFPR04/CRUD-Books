from tkinter import * 
from CRUDbooktable import crud

root = Tk()
root.title("Librería Pepe")
root.geometry("500x400")

title = Label(root, text="Librería Pepe").grid(column=1, row=0)
crudbutton = Button(root, text="Book table", command=crud).grid(column=0,row=1)

root.mainloop()