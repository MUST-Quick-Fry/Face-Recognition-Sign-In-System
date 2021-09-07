import sqlite3

with sqlite3.connect('stuDB.sqlite3') as con:
    mycursor = con.cursor()
    sql_command = "SELECT * FROM stuInfo"
    mycursor.execute(sql_command)

    print(mycursor.fetchall())