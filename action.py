import sqlite3
import atexit
import printdb
import sys

connect = sqlite3.connect('moncafe.db')


def close_db():
    connect.commit()
    connect.close()


atexit.register(close_db)


def has_enough_and_quantity(cursor, product_id, activity_quantity):
    cursor.execute("""SELECT Products.quantity From Products WHERE Products.id = (?)
    """, [product_id])
    quantity = int(cursor.fetchone()[0])
    return quantity + activity_quantity >= 0, quantity


input_config_name = sys.argv[1]
cursor = connect.cursor()
with open(input_config_name) as input_config:
    input_config = input_config.read().splitlines()
    for line in input_config:
        line = line.split(", ")
        has_enough, current_quantity = has_enough_and_quantity(cursor, int(line[0]), int(line[1]))
        if int(line[1]) != 0 and has_enough:
            cursor.execute("""
                INSERT INTO Activities (product_id,quantity,activator_id,date) VALUES (?,?,?,?)""",
                           [int(line[0]), int(line[1]), int(line[2]), line[3]])
            cursor.execute("""UPDATE Products SET quantity = ? WHERE id = ?""",
                           [int(line[1]) + current_quantity, int(line[0])])

printdb.print_db(connect)
