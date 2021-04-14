import sqlite3
import datetime


class DataBase:
    def __init__(self):
        self.db = sqlite3.connect("users.db")
        self.sql = self.db.cursor()
        try:
            self.sql.execute("""CREATE TABLE users
                                  (id, mark, date)
                               """)
        except Exception as e:
            pass

        try:
            self.sql.execute("""CREATE TABLE message
                                  (id, text, ans INT)
                               """)
        except Exception as e:
            pass

        try:
            self.sql.execute("""CREATE TABLE matrix
                                  (id, param1, param2, param3, positive, negative, neutral)
                               """)
        except:
            pass

    def AddUser(self, id):
        self.sql.execute(f""" SELECT id FROM users WHERE id = {id} """)
        if self.sql.fetchone() is None:
            # self.sql.execute("SELECT id FROM users")
            self.sql.execute(f"INSERT INTO users VALUES (?, ?, ?)", (id, '0', datetime.date.today()))
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

    def setAns(self, idAns, ans):
        try:
            self.sql.execute(f'SELECT ans FROM message WHERE id = {idAns} ')
            an = str(self.sql.fetchone())
            an = an.replace('(', '')
            an = an.replace(',', '')
            an = an.replace(')', '')
            a = int(an)
            self.sql.execute(f' UPDATE message SET ans = {ans} WHERE id = {idAns} ')
        except:
            pass
        self.db.commit()

    def getAns(self, idA):
        try:
            self.sql.execute(f'SELECT ans FROM message WHERE id = {idA} ')
            an = str(self.sql.fetchone())
            an = an.replace('(', '')
            an = an.replace(',', '')
            an = an.replace(')', '')
            try:
                return int(an)
            except:
                return 0
        except Exception as e:
            print(e)

    def getAll(self):
        try:
            self.sql.execute(f'SELECT id FROM users')
            id = self.sql.fetchall()
            ids = []
            for i in id:
                i.replace('(', '')
                i.replace(',', '')
                i.replace(')', '')
                ids.append(i)
            return ids
        except Exception as e:
            print(e)

    def getText(self):
        self.sql.execute("SELECT u.rowid, u.id, m.text FROM users u LEFT JOIN message m ON m.id = u.id")
        texts = []
        dbTexts = self.sql.fetchall()
        for i, el in enumerate(dbTexts):
            try:
                if dbTexts[i][0] == dbTexts[i + 1][0]:
                    dbTexts.pop(i)
            except:
                pass
        for el in dbTexts:
            texts.append(str(el[2]))
        return texts

    # message
    def AddMessage(self, idMes, text):
        try:
            self.sql.execute(f"SELECT id FROM message WHERE id = '{idMes}' ")
            if self.sql.fetchone() is None:
                self.sql.execute("SELECT id FROM users")
                self.sql.execute(f"INSERT INTO message VALUES (?, ?, ?)", (idMes, text, -1))
        except:
            pass
        self.db.commit()

    def AddRes(self, id, param1, param2, param3, positive, negative, neutral):
        # self.sql.execute("SELECT rowid, param1, param2, param3 FROM matrix")
        try:
            self.sql.execute(
                f"UPDATE matrix SET param1 = {param1}, param2 = {param2}, param3 = {param3}, positive = {positive}, negative = {negative}, neutral = {neutral} WHERE id = {id}")
        except Exception as e:
            print(e)
        self.db.commit()

    def setParam1(self, id, param1):
        try:
            self.sql.execute(f"UPDATE matrix SET param1 = {param1} WHERE id = {id}")
        except Exception as e:
            print(e)
        self.db.commit()

    def setParam2(self, id, param2):
        try:
            self.sql.execute(f"UPDATE matrix SET param2 = {param2} WHERE id = {id}")
        except Exception as e:
            print(e)
        self.db.commit()

    def setParam3(self, id, param3):
        try:
            self.sql.execute(f"UPDATE matrix SET param3 = '{param3}' WHERE id = {id}")
        except Exception as e:
            print(e)
        self.db.commit()

    def setPos(self, id, positive):
        try:
            self.sql.execute(f"UPDATE matrix SET positive = {positive} WHERE id = {id}")
        except Exception as e:
            print(e)
        self.db.commit()

    def setNegativ(self, id, negative):
        try:
            self.sql.execute(f"UPDATE matrix SET negative = {negative} WHERE id = {id}")
        except Exception as e:
            print(e)
        self.db.commit()

    def setNeutral(self, id, neutral):
        try:
            self.sql.execute(f"UPDATE matrix SET neutral = {neutral} WHERE id = {id}")
        except Exception as e:
            print(e)
        self.db.commit()

    def AddID(self, id):
        try:
            self.sql.execute(f"SELECT id FROM matrix WHERE id = {id}")
            if self.sql.fetchone() is None:
                self.sql.execute(f"INSERT INTO matrix VALUES (?, ?, ?, ?, ?, ?, ?)", (id, 0, 0, 0, 0, 0, 0))
        except Exception as e:
            print(e)
        self.db.commit()
