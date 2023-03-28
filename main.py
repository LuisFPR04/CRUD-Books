from tkinter import *
import sqlite3

con = sqlite3.connect("booktable.db")
cur = con.cursor()
try:
    cur.execute("CREATE TABLE books (Name varchar(30) UNIQUE, Author varchar(30), Publisher varchar(10), Price int(3), ReleaseDate year, PageNumber int(4))")
except: pass

#Funciones

def submit():
    con = sqlite3.connect("booktable.db")
    con.cursor()

    con.execute("INSERT INTO books (Name, Author, Publisher, Price, ReleaseDate, PageNumber) VALUES(:Name, :Author, :Publisher, :Price, :ReleaseDate, :PageNumber)",
                {
                    'Name': Name.get(),
                    'Author': Author.get(),
                    'Publisher': Publisher.get(),
                    'Price': int(Price.get()),
                    'ReleaseDate': ReleaseDate.get(),
                    'PageNumber': int(PageNumber.get())
                })

    con.commit()
    con.close()

    Name.delete(0, END)
    Author.delete(0, END)
    Publisher.delete(0, END)
    Price.delete(0, END)
    ReleaseDate.delete(0, END)
    PageNumber.delete(0, END)

def query():
    res = cur.execute("SELECT * FROM books")
    text = ""
    for row in res:
        text += f"{row[0]}, {row[1]}, {row[2]}, {row[3]}, {row[4]}, {row[5]} \n"

    query_label = Label(root, text=text).grid(row=0, columnspan=2, column=1)

root = Tk()
root.title("CRUD Books")
root.iconbitmap("book_icon.png")

#Botones y cajas de texto
Name = Entry(root, width=30)
Name.grid(row=1, column=0, padx=20)
Author = Entry(root, width=30)
Author.grid(row=3, column=0, padx=20)
Publisher = Entry(root, width=30)
Publisher.grid(row=5, column=0, padx=20)
Price = Entry(root, width=30)
Price.grid(row=7, column=0, padx=20)
ReleaseDate = Entry(root, width=30)
ReleaseDate.grid(row=9, column=0, padx=20)
PageNumber = Entry(root, width=30)
PageNumber.grid(row=11, column=0, padx=20)

name_label = Label(root, text="Book name").grid(row=0, column=0)
author_label = Label(root, text="Author name").grid(row=2, column=0)
publisher_label = Label(root, text="Publisher").grid(row=4, column=0)
price_label = Label(root, text="Book's price").grid(row=6, column=0)
ReleaseDate_label = Label(root, text="Release Date (YYYY)").grid(row=8, column=0)
PageNumber_label = Label(root, text="Number of pages").grid(row=10, column=0)

submit_button = Button(root, text="Add to book Database", command=submit).grid(row=13,column = 0, columnspan=2, pady=10, padx=10)
query_button = Button(root, text="Show records", command=query).grid(row=14,column = 0, columnspan=2, pady=10, padx=10)

root.geometry("800x400")
con.commit()
root.mainloop()

def ReadBooks():
    res = cur.execute("SELECT * FROM books")
    for row in res:
        print(f"{row[0]}, {row[1]}, {row[2]}, {row[3]}, {row[4]}, {row[5]}")
ReadBooks()
