import sqlite3


def print_db(connection):
    cursor = connection.cursor()
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

    # printing Employees report

    cursor.execute("""
              select Employees.name, Employees.salary, Coffee_stands.location, ifnull(sum((-Activities.quantity) * Products.price),0) from Employees
              left join Activities on Activities.activator_id = Employees.id
              left join Coffee_stands on Employees.coffee_stand = Coffee_stands.id
              left join Products on Products.id = Activities.product_id
              GROUP by Employees.id ORDER by Employees.name""")
    print("\nEmployees report")
    for record in cursor:
        sdtr = " ".join([str(attribute) for attribute in record])
        print(sdtr)

    # printing Activities report
    cursor.execute("""
              SELECT Activities.date, Products.description, Activities.quantity, Employees.name, Suppliers.name from Activities
            LEFT JOIN Products on Products.id = Activities.product_id
            LEFT JOIN Employees on Employees.id = Activities.activator_id
            LEFT JOIN Suppliers on Suppliers.id = Activities.activator_id
            ORDER BY date
    """)

    fetchall = cursor.fetchall()
    if len(fetchall) > 0:
        print("\nActivities")
        for record in fetchall:
            print(record)


if __name__ == '__main__':
    connect = sqlite3.connect("moncafe.db")
    print_db(connect)
