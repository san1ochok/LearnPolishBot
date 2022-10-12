import sqlite3
import datetime

con = sqlite3.connect('cache/.db')
cursor = con.cursor()


def CreateDB():
    print(f"Connected to Sqlite")
    cursor = con.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS users (
        name TEXT, 
        id INTEGER PRIMARY KEY,
        joiningDate timestamp
        )""")
    con.commit()


def UpdateValue(val_name, new_val, id):
    for row in cursor.execute(f"SELECT {val_name} FROM users where id={id}"):
        new = row[0] + new_val
        cursor.execute(f"UPDATE users SET {val_name}={new} where id={id}")
        con.commit()


def InsertValue(name, id, joiningDate):
    cursor.execute(
        f"INSERT INTO users VALUES ('{name}', {id}, '{joiningDate}')")
    con.commit()

