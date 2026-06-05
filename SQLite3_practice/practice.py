import sqlite3

# print(dir(sqlite3))

connection = sqlite3.connect("todoList.db")

cursor = connection.cusrsor()

cursor.excute(""" CREATE TABLE 
tasks( to_Do text,
        in_progress text,
        done text,
        history_tasks text
        )""")

connection.commit()
connection.close()