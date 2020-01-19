import sqlite3

connect = sqlite3.connect("moncafe.db")
cursor = connect.cursor()

cursor.execute("SELECT * FROM Activities ORDER BY date")
print('Activities')
for record in cursor.fetchall():
    print(record)

cursor.execute("SELECT * FROM Coffee_stands ORDER BY id")
print('Coffee stands')
for record in cursor.fetchall():
    print(record)

cursor.execute("SELECT * FROM Employees ORDER BY id")
print('Employees')
for record in cursor.fetchall():
    print(record)

cursor.execute("SELECT * FROM Products ORDER BY id")
print('Products')
for record in cursor.fetchall():
    print(record)

cursor.execute("SELECT * FROM Suppliers ORDER BY id")
print('Suppliers')
for record in cursor.fetchall():
    print(record)
