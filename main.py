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
    Name = ""
    Author = ""
    Publisher = ""
    Price = ""
    ReleaseDate = ""
    PageNumber = ""
    for row in res:
        Name += f"{row[0]}\n"
        Author += f"{row[1]}\n"
        Publisher += f"{row[2]}\n"
        Price += f"{row[3]}\n"
        ReleaseDate += f"{row[4]}\n"
        PageNumber += f"{row[5]}\n"


    name_frame = Frame(root)
    author_frame = Frame(root)
    publisher_frame = Frame(root)
    price_frame = Frame(root)
    release_date_frame = Frame(root)
    page_number_frame = Frame(root)

    name_frame.grid(row=4, column=0)
    author_frame.grid(row=4, column=1)
    publisher_frame.grid(row=4, column=2)
    price_frame.grid(row=4, column=3)
    release_date_frame.grid(row=4, column=4)
    page_number_frame.grid(row=4, column=5)

    name_label = Label(name_frame, text="Name").grid(row=0, column=0)
    author_label = Label(author_frame, text="Author").grid(row=0, column=0)
    publisher_label = Label(publisher_frame, text="Publisher").grid(row=0, column=0)
    price_label = Label(price_frame, text="Price (US Dolar)").grid(row=0, column=0)
    release_date_label = Label(release_date_frame, text="Release Date").grid(row=0, column=0)
    page_number_label = Label(page_number_frame, text="Page Number").grid(row=0, column=0)

    name_data = Label(name_frame, text=Name).grid(row=1, column=0)
    author_data = Label(author_frame, text=Author).grid(row=1, column=0)
    publisher_data = Label(publisher_frame, text=Publisher).grid(row=1, column=0)
    price_data = Label(price_frame, text=Price).grid(row=1, column=0)
    release_date_data = Label(release_date_frame, text=ReleaseDate).grid(row=1, column=0)
    page_number_data = Label(page_number_frame, text=PageNumber).grid(row=1, column=0)  

def delete(value1, value2):
    con = sqlite3.connect("booktable.db")
    con.cursor()

    if type(value2) == str:
        cur.execute(f"DELETE FROM BOOKS WHERE {value1} = '{value2}'")
    if type(value2) == int:
        cur.execute(f"DELETE FROM BOOKS WHERE {value1} > {value2}")

    con.commit()
    con.close()

def update():
    print("Something")

root = Tk()
root.title("CRUD Books")
root.iconbitmap("book_icon.png")
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
#Botones y cajas de texto

Name = Entry(root, width=30)
Name.grid(row=1, column=0, padx=20)
Author = Entry(root, width=30)
Author.grid(row=1, column=1, padx=20)
Publisher = Entry(root, width=30)
Publisher.grid(row=1, column=2, padx=20)
Price = Entry(root, width=30)
Price.grid(row=1, column=3, padx=20)
ReleaseDate = Entry(root, width=30)
ReleaseDate.grid(row=1, column=4, padx=20)
PageNumber = Entry(root, width=30)
PageNumber.grid(row=1, column=5, padx=20)

name_label = Label(root, text="Book name").grid(row=0, column=0)
author_label = Label(root, text="Author name").grid(row=0, column=1)
publisher_label = Label(root, text="Publisher").grid(row=0, column=2)
price_label = Label(root, text="Book's price (US Dolar)").grid(row=0, column=3)
ReleaseDate_label = Label(root, text="Release Date (YYYY)").grid(row=0, column=4)
PageNumber_label = Label(root, text="Number of pages").grid(row=0, column=5)

submit_button = Button(root, text="Add to book Database", command=submit).grid(row=2,column = 0, pady=10, padx=10)
delete_button = Button(root, text="Delete from book Database", command=delete).grid(row=2,column = 1, pady=10, padx=10)
update_button = Button(root, text="Update from book Database", command=update).grid(row=2,column = 2, pady=10, padx=10)
query_button = Button(root, text="Show records", command=query).grid(row=2,column = 3, pady=10, padx=10)

con.commit()
root.mainloop()
