import sqlite3


con = sqlite3.connect("booktable.db")
cur = con.cursor()
try:
    cur.execute("CREATE TABLE books (Name varchar(30) UNIQUE, Author varchar(30), Publisher varchar(10), Price int(3), ReleaseDate year, PageNumber int(4))")
except: pass

def AddBooks(Name, Author, Publisher, Price, RealeseDate, PageNumber):
    try:
        cur.execute(f"INSERT INTO books (Name, Author, Publisher, Price, ReleaseDate, PageNumber) VALUES ('{Name}', '{Author}', '{Publisher}', {Price}, '{RealeseDate}', {PageNumber})")
        con.commit()
    except: print("Value already exists")

def DelBooks(value1, value2):
    if type(value2) == str:
        cur.execute(f"DELETE FROM BOOKS WHERE {value1} = '{value2}'")
    if type(value2) == int:
        cur.execute(f"DELETE FROM BOOKS WHERE {value1} > {value2}")
    con.commit()
    
#def UpdateBooks(value1, value2, value3):
#    cur.execute(f"UPDATE Books SET {value1} = '{value2}' WHERE = {value3}")

def ReadBooks():
    res = cur.execute("SELECT * FROM books")
    #print(res.fetchall())
    for row in res:
        print(row[0])
