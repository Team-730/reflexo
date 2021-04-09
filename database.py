import sqlite3
import datetime


class DataBase:
    def __init__(self):
        self.db = sqlite3.connect("users.db")
        self.sql = self.db.cursor()
        try:
            self.sql.execute("""CREATE TABLE users
                                  (id, color, text, date)
                               """)
        except Exception as e:
            pass

        try:
            self.sql.execute("""CREATE TABLE message
                                  (id, text, date)
                               """)
        except Exception as e:
            pass

        try:
            self.sql.execute("""CREATE TABLE matrix
                                  (res)
                               """)
        except Exception as e:
            pass


    def AddUser(self, id):
        self.sql.execute(f""" SELECT id FROM users WHERE id = {id} """)
        if self.sql.fetchone() == None:
            # self.sql.execute("SELECT id FROM users")
            self.sql.execute(f"INSERT INTO users VALUES (?, ?, ?, ?)", (id, '', '', datetime.date.today()))
        self.db.commit()

    def setData(self, id, date):
        try:
            self.sql.execute(f'SELECT id FROM users WHERE id = "{id}" ')
            if self.sql.fetchone() is None:
                pass
            else:
                self.sql.execute(f' UPDATE users SET date = "{date}" WHERE id = "{id}" ')
        except:
            pass
        self.db.commit()

    def setColor(self, id, color):
        try:
            self.sql.execute(f'SELECT id FROM users WHERE id = "{id}" ')
            if self.sql.fetchone() is None:
                pass
            else:
                self.sql.execute(f' UPDATE users SET color = "{color}" WHERE id = "{id}" ')
        except:
            pass
        self.db.commit()

    def setText(self, id, text):
        try:
            self.sql.execute(f'SELECT id FROM users WHERE id = "{id}" ')
            if self.sql.fetchone() is None:
                pass
            else:
                self.sql.execute(f' UPDATE users SET text = "{text}" WHERE id = "{id}" ')
        except Exception as e:
            print(e)
        self.db.commit()

    def getAll(self):
        try:
            self.sql.execute(f'SELECT id FROM users')
            id = self.sql.fetchall()
            return id
        except Exception as e:
            print(e)

    def getText(self):
        self.sql.execute("SELECT u.rowid, u.id, m.text FROM users u LEFT JOIN message m ON m.id = u.id")
        texts = []
        dbTexts = self.sql.fetchall()
        for i, el in enumerate(dbTexts):
            try:
                if dbTexts[i][0] == dbTexts[i+1][0]:
                    dbTexts.pop(i)
            except:
                pass
        for el in dbTexts:
            texts.append(str(el[2]))
        print(texts)
        return texts

    #message
    def AddMessage(self, id, text):
        try:
            self.sql.execute(f"SELECT id FROM message WHERE id = '{id}' ")
            if self.sql.fetchone() is None:
                self.sql.execute("SELECT id FROM users")
                self.sql.execute(f"INSERT INTO message VALUES (?, ?, ?, ?)", (id, '', text, datetime.date.today()))

        except:
            pass
        self.db.commit()

    def AddRes(self, num, res):
        try:
            self.sql.execute(f"SELECT res FROM matrix WHERE rowid = {num} ")
            if self.sql.fetchone() is None:
                self.sql.execute("SELECT res FROM matrix")
                self.sql.execute(f"INSERT INTO matrix VALUES (?)", (res))
            else:
                self.sql.execute("UPDATE matrix SET res = '{res}' WHERE rowid = {num}")

        except:
            pass
        self.db.commit()
