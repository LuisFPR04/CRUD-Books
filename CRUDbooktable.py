from tkinter import *
import sqlite3

def crud():
        
    con = sqlite3.connect("booktable.db")
    cur = con.cursor()
    try:
        cur.execute("CREATE TABLE books (ID INTEGER PRIMARY KEY AUTOINCREMENT, Name VARCHAR(50) UNIQUE, Author VARCHAR(50), Publisher VARCHAR(50), Price INTEGER, ReleaseDate DATE, PageNumber INTEGER)")
    except: pass

    #Funciones

    def submit():
        con = sqlite3.connect("booktable.db")
        cur = con.cursor()


        cur.execute("INSERT INTO books (Name, Author, Publisher, Price, ReleaseDate, PageNumber) VALUES(:Name, :Author, :Publisher, :Price, :ReleaseDate, :PageNumber)",
                    {
                        'Name': Name.get(),
                        'Author': Author.get(),
                        'Publisher': Publisher.get(),
                        'Price': int(Price.get()),
                        'ReleaseDate': ReleaseDate.get(),
                        'PageNumber': int(PageNumber.get())
                    })

        con.commit()
        cur.close()
        con.close()

        Name.delete(0, END)
        Author.delete(0, END)
        Publisher.delete(0, END)
        Price.delete(0, END)
        ReleaseDate.delete(0, END)
        PageNumber.delete(0, END)

    def query():
        res = cur.execute("SELECT * FROM books")
        id = ""
        Name = ""
        Author = ""
        Publisher = ""
        Price = ""
        ReleaseDate = ""
        PageNumber = ""
        for row in res:
            id += f"{row[0]}\n"
            Name += f"{row[1]}\n"
            Author += f"{row[2]}\n"
            Publisher += f"{row[3]}\n"
            Price += f"{row[4]}\n"
            ReleaseDate += f"{row[5]}\n"
            PageNumber += f"{row[6]}\n"


        id_frame = Frame(root)
        name_frame = Frame(root)
        author_frame = Frame(root)
        publisher_frame = Frame(root)
        price_frame = Frame(root)
        release_date_frame = Frame(root)
        page_number_frame = Frame(root)

        id_frame.grid(row=12, column=0)
        name_frame.grid(row=12, column=1)
        author_frame.grid(row=12, column=2)
        publisher_frame.grid(row=12, column=3)
        price_frame.grid(row=12, column=4)
        release_date_frame.grid(row=12, column=5)
        page_number_frame.grid(row=12, column=6)

        id_label = Label(id_frame, text="ID").grid(row=0, column=0)
        name_label = Label(name_frame, text="Name").grid(row=0, column=0)
        author_label = Label(author_frame, text="Author").grid(row=0, column=0)
        publisher_label = Label(publisher_frame, text="Publisher").grid(row=0, column=0)
        price_label = Label(price_frame, text="Price (US Dolar)").grid(row=0, column=0)
        release_date_label = Label(release_date_frame, text="Release Date").grid(row=0, column=0)
        page_number_label = Label(page_number_frame, text="Number of pages").grid(row=0, column=0)

        id_label = Label(id_frame, text=id).grid(row=1, column=0)
        name_data = Label(name_frame, text=Name).grid(row=1, column=0)
        author_data = Label(author_frame, text=Author).grid(row=1, column=0)
        publisher_data = Label(publisher_frame, text=Publisher).grid(row=1, column=0)
        price_data = Label(price_frame, text=Price).grid(row=1, column=0)
        release_date_data = Label(release_date_frame, text=ReleaseDate).grid(row=1, column=0)
        page_number_data = Label(page_number_frame, text=PageNumber).grid(row=1, column=0)  

    def delete():
        con = sqlite3.connect("booktable.db")
        cur = con.cursor()

        if type(CampDel_label.get()) == str:
            cur.execute(f"DELETE FROM BOOKS WHERE {selected_optionDel.get()} = '{CampDel_label.get()}'")
        if type(CampDel_label.get()) == int:
            cur.execute(f"DELETE FROM BOOKS WHERE {selected_optionDel.get()} > {CampDel_label.get()}")

        con.commit()
        cur.close()
        con.close()

    def update():
        con = sqlite3.connect("booktable.db")
        cur = con.cursor()
        if type(CampUP.get()) == str and type(CampUP2.get() == str):
            cur.execute(f"UPDATE Books SET {selected_optionUp1.get()} = '{CampUP.get()}' WHERE {selected_optionUp2.get()} = '{CampUP2.get()}'")
        elif type(CampUP2.get()) == int:
            cur.execute(f"UPDATE Books SET {selected_optionUp1.get()} = '{CampUP.get()}' WHERE {selected_optionUp2.get()} = {CampUP2.get()}")
        elif type(CampUP2.get()) == str:
            cur.execute(f"UPDATE Books SET {selected_optionUp1.get()} = {CampUP.get()} WHERE {selected_optionUp2.get()} = '{CampUP2.get()}'")
        elif type(CampUP.get()) == int and type(CampUP2.get() == int):
            cur.execute(f"UPDATE Books SET {selected_optionUp1.get()} = {CampUP.get()} WHERE {selected_optionUp2.get()} = {CampUP2.get()}")
        con.commit()
        cur.close()
        con.close()

    root = Tk()
    root.title("CRUD Books")
    root.iconbitmap("book_icon.png")
    root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
    #Botones y cajas de texto
    selected_optionDel = StringVar()
    selected_optionUp1 = StringVar()
    selected_optionUp2 = StringVar()
    options = ["Book name", "Author", "Publisher", "Price", "ReleaseDate", "PageNumber"]

    #Entry text camp
    Name = Entry(root, width=20)
    Name.grid(row=3, column=0, padx=10)
    Author = Entry(root, width=20)
    Author.grid(row=3, column=1, padx=10)
    ReleaseDate = Entry(root, width=20)
    ReleaseDate.grid(row=3, column=2, padx=10)
    Publisher = Entry(root, width=20)
    Publisher.grid(row=5, column=0, padx=10)
    Price = Entry(root, width=20)
    Price.grid(row=5, column=1, padx=10)
    PageNumber = Entry(root, width=20)
    PageNumber.grid(row=5, column=2, padx=10)

    #MDropdown menus
    dropdownReference= OptionMenu(root, selected_optionUp2, *options).grid(row=3, column=4, padx=20) #The conditional 'where' on the SQL command
    dropdownUpdate = OptionMenu(root, selected_optionUp1, *options).grid(row=3, column=5, padx=20) #The one that makes reference to what is change
    dropdownDel = OptionMenu(root, selected_optionDel, *options).grid(row=3, column=7, padx=20)

    #Delete text camp
    CampDel_label = Entry(root, width=30)
    CampDel_label.grid(row=3, column=8, padx=20)

    #Update camps
    CampUP2 = Entry(root, width=30)
    CampUP2.grid(row=5, column=4, padx=20)
    CampUP = Entry(root, width=30)
    CampUP.grid(row=5, column=5, padx=20)

    #Entry labels
    title_submit_label = Label(root, text="Submit camps").grid(row=1,column = 1, pady=10, padx=10)
    name_label = Label(root, text="Book name").grid(row=2, column=0)
    author_label = Label(root, text="Author name").grid(row=2, column=1)
    publisher_label = Label(root, text="Publisher").grid(row=4, column=0)
    price_label = Label(root, text="Book's price (US Dolar)").grid(row=4, column=1)
    ReleaseDate_label = Label(root, text="Publication Date (YYYY)").grid(row=2, column=2)
    PageNumber_label = Label(root, text="Number of pages").grid(row=4, column=2)

    #Update label
    title_update_label = Label(root, text="Update camps").grid(row=1, column=4, pady=10, padx=10,columnspan=2)
    CampName_label = Label(root, text="Camp name to reference").grid(row=2, column=4, columnspan=1)
    SelecUp_label = Label(root, text="Camp to update").grid(row=2, column=5)
    SelecValue_label = Label(root, text="Updated value").grid(row=4, column=5)
    SelecValueWhere= Label(root, text="Reference value").grid(row=4, column=4)

    #Delete label
    title_delete_label = Label(root, text="Delete camps").grid(row=1, column=6, pady=10, padx=10,columnspan=3)
    CampDel_label = Label(root, text="Camp name to reference").grid(row=2, column=7)
    SelecDel_label = Label(root, text="Camp to delete").grid(row=2, column=8, columnspan=2)

    #Separators
    hr_separator1 = Frame(root, height=2, bd=1, relief=RIDGE)
    hr_separator2 = Frame(root, height=2, bd=1, relief=RIDGE)
    hr_separator1.grid(row=0, column=0, columnspan=9, sticky="we")
    hr_separator2.grid(row=7, column=0, columnspan=9, sticky="we")

    vertical_separator1 = Frame(root, width=2, bd=1, relief=RIDGE)
    vertical_separator2 = Frame(root, width=2, bd=1, relief=RIDGE)
    vertical_separator3 = Frame(root, width=2, bd=1, relief=RIDGE)
    vertical_separator1.grid(row=0, column=3, rowspan=7, sticky="ns")
    vertical_separator2.grid(row=0, column=6, rowspan=7, sticky="ns")
    vertical_separator3.grid(row=0, column=9, rowspan=7, sticky="ns")
    #Buttons

    submit_button = Button(root, text="Add to book Database", command=submit).grid(row=6,column = 1, pady=10, padx=10)
    delete_button = Button(root, text="Delete from book Database", command=delete).grid(row=6,column = 7, pady=10, padx=10, columnspan=2)
    update_button = Button(root, text="Update Database", command=update).grid(row=6,column = 4, pady=10, padx=10, columnspan=2)
    query_button = Button(root, text="Show records", command=query).grid(row=8,column = 1, pady=10, padx=10)

    con.commit()
    root.mainloop()

crud()

