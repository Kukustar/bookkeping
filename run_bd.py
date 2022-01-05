import sqlite3

conn = sqlite3.connect("app/db.sqlite3")
cursor = conn.cursor()


def insert_purchase_into_table(file_name):
    with open(file_name) as file:
        for line in file:
            # print(line)
            cursor.execute(line)
    conn.commit()


insert_purchase_into_table('purchase.sql')


def insert_deposit_into_table(file_name):
    with open(file_name) as file:
        for line in file:
            # print(line)
            cursor.execute(line)
    conn.commit()


insert_deposit_into_table("deposit.sql")


def get_table_purchases_data():
    sql = "SELECT count(*) FROM purchases_purchase"
    cursor.execute(sql)
    print("Purchase count", cursor.fetchone()[0])


get_table_purchases_data()

def get_table_deposit_data():
    sql = "SELECT count(*) FROM purchases_deposit"
    cursor.execute(sql)
    print("Deposit count", cursor.fetchone()[0])


get_table_deposit_data()
conn.close()


