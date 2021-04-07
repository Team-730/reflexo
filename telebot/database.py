import sqlite3
import datetime


db = sqlite3.connect("users.db")
sql = db.cursor()
try:
    sql.execute("""CREATE TABLE users
                      (id, color, text, date)
                   """)
except Exception as e:
    pass

try:
    sql.execute("""CREATE TABLE message
                      (id, text)
                   """)
except Exception as e:
    pass


def AddUser(id):
    db = sqlite3.connect("users.db")
    sql = db.cursor()
    try:
        sql.execute(f"SELECT id FROM users WHERE id = '{id}' ")
        if sql.fetchone() is None:
            sql.execute("SELECT id FROM users")
            sql.execute(f"INSERT INTO users VALUES (?, ?, ?, ?)", (id, '', '', datetime.date.today()))

    except:
        sql.execute("SELECT id FROM users")
        sql.execute(f"INSERT INTO users VALUES (?, ?, ?, ?)", (id, '', '', datetime.date.today()))
    db.commit()

def setData(id, date):
    db = sqlite3.connect("users.db")
    sql = db.cursor()
    try:
        sql.execute(f'SELECT id FROM users WHERE id = "{id}" ')
        if sql.fetchone() is None:
            pass
        else:
            sql.execute(f' UPDATE users SET date = "{date}" WHERE id = "{id}" ')
    except:
        pass
    db.commit()

def setColor(id, color):
    db = sqlite3.connect("users.db")
    sql = db.cursor()
    try:
        sql.execute(f'SELECT id FROM users WHERE id = "{id}" ')
        if sql.fetchone() is None:
            pass
        else:
            sql.execute(f' UPDATE users SET color = "{color}" WHERE id = "{id}" ')
    except:
        pass
    db.commit()

def setText(id, text):
    db = sqlite3.connect("users.db")
    sql = db.cursor()
    try:
        sql.execute(f'SELECT id FROM users WHERE id = "{id}" ')
        if sql.fetchone() is None:
            pass
        else:
            sql.execute(f' UPDATE users SET text = "{text}" WHERE id = "{id}" ')
    except Exception as e:
        print(e)
    db.commit()

def getAll():
    try:
        db = sqlite3.connect("users.db")
        sql = db.cursor()
        sql.execute(f'SELECT num, id FROM users ORDER BY num')
        return sql.fetchall()
    except:
        pass


def getId(num):
    try:
        db = sqlite3.connect("users.db")
        sql = db.cursor()
        sql.execute(f'SELECT id FROM users WHERE num = {num} ')
        id = sql.fetchone()
        print(sql.fetchall())
        return id[num]
    except:
        pass

#message
def AddMessage(id, text):
    db = sqlite3.connect("users.db")
    sql = db.cursor()
    try:
        sql.execute(f"SELECT id FROM message WHERE id = '{id}' ")
        if sql.fetchone() is None:
            sql.execute("SELECT id FROM users")
            sql.execute(f"INSERT INTO message VALUES (?, ?)", (id, text))

    except:
        sql.execute("SELECT id FROM users")
        sql.execute(f"INSERT INTO users VALUES (?, ?)", (id, text))
    db.commit()
