import sqlite3

conn = sqlite3.connect("app/db.sqlite3")
cursor = conn.cursor()


def insert_into_table():
    with open("file.sql") as files:
        for line in files:
            print(line)
            cursor.execute(line)
    conn.commit()


insert_into_table()


def get_table_data():
    sql = "SELECT * FROM purchases_purchase"
    cursor.execute(sql)
    for row in cursor.execute("SELECT rowid, * FROM purchases_purchase"):
        print(row)
    return row


get_table_data()
