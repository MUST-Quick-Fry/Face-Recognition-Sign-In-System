import sqlite3

class SQLITE3_Helper:
    def __init__(self):
        self.db = 'stuDB.sqlite3'

    def query(self, cmd):
        with sqlite3.connect(self.db) as con:
            mycursor = con.cursor()
            mycursor.execute(cmd)
            #self.display()

        return mycursor.fetchall()

    def insert(self, cmd):
        with sqlite3.connect(self.db) as con:
            mycursor = con.cursor()
            mycursor.execute(cmd)
            self.display()

    def display(self):
        with sqlite3.connect(self.db) as con:
            sqlstr = "SELECT * FROM tasks_student"
            mycursor = con.cursor()
            mycursor.execute(sqlstr)

            print(mycursor.fetchall())