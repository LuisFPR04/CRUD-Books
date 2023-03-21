import sqlite3

con = sqlite3.connect("booktable.db")
cur = con.cursor()

try:
    #cur.execute("CREATE TABLE books (Name varchar(30) UNIQUE, Author varchar(30), Publisher varchar(10), Price int(3), ReleaseDate year, PageNumber int(4))")
    cur.execute("INSERT INTO books (Name, Author, Publisher, Price, ReleaseDate, PageNumber) VALUES ('Shadows of Self', 'Brandon Sanderson', 'Nova', 30, '2015', 437)")
    con.commit()
except: print("Value already exists")

res = cur.execute("SELECT * FROM books")

print(res.fetchall())