import atexit
import sqlite3
import sys
import os

if os.path.isfile("moncafe.db"):
    os.remove("moncafe.db")

connect = sqlite3.connect('moncafe.db')

def close_db():
    connect.commit()
    connect.close()


atexit.register(close_db)

connect.executescript("""
                        CREATE TABLE Employees(
                        id INTEGER PRIMARY KEY,
                        name TEXT NOT NULL,
                        salary REAL NOT NULL,
                        coffee_stand INTEGER REFERENCES Coffee_stand(id)
                        );
                            
                    
                        CREATE TABLE Suppliers(
                        id INTEGER PRIMARY KEY,
                        name TEXT NOT NULL,
                        contact_information TEXT
                        );
                           
                        CREATE TABLE Products(
                        id INTEGER PRIMARY KEY,
                        description TEXT NOT NULL,
                        price REAL NOT NULL,
                        quantity INTEGER NOT NULL
                        );
                           
                        CREATE TABLE Coffee_stands(
                        id INTEGER PRIMARY KEY,
                        location TEXT NOT NULL,
                        number_of_employees INTEGER
                        );
                           
                        CREATE TABLE Activities(
                        product_id INTEGER REFERENCES Product(id),
                        quantity INTEGER NOT NULL,
                        activator_id INTEGER NOT NULL REFERENCES Suppliers(id) REFERENCES Employees(id),
                        date DATE NOT NULL
                        );
                        
                        CREATE TABLE Employees_report( 
                        name TEXT REFERENCES Employees(name),
                        salary REAL NOT NULL REFERENCES Employees(salary),
                        working location TEXT NOT NULL REFERENCES Coffee_stands(location),
                        total_sales INTEGER
                        );
                        
                        """)

input_config_name = sys.argv[1]
cursor = connect.cursor()

with open(input_config_name) as input_config:
    input_config = input_config.read().splitlines()
    for line in input_config:
        line = line.split(", ")
        if line[0] == 'E':
            cursor.execute("""
            INSERT INTO Employees (id, name, salary, coffee_stand) VALUES (?,?,?,?)
            """, [int(line[1]), line[2], float(line[3]), int(line[4])])
        elif line[0] == 'S':
            cursor.execute("""
            INSERT INTO Suppliers (id, name, contact_information) VALUES (?,?,?)
            """, [int(line[1]), line[2], line[3]])
        elif line[0] == 'P':
            cursor.execute("""
            INSERT INTO Products (id, description, price, quantity) VALUES (?,?,?,?)
            """, [int(line[1]), line[2], float(line[3]), 0])
        elif line[0] == 'C':
            cursor.execute("""
            INSERT INTO Coffee_stands (id, location, number_of_employees) VALUES (?,?,?)
            """, [int(line[1]), line[2], int(line[3])])
