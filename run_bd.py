import sqlite3

conn = sqlite3.connect("app/db.sqlite3")
cursor = conn.cursor()


def insert_into_table(file_name):
    with open(file_name) as file:
        for line in file:
            cursor.execute(line)
    conn.commit()


insert_into_table('purchase_balance.sql')


conn.close()

