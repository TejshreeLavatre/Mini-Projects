#Python program to create a table and enter data with SQL

import sqlite3
connection = sqlite3.connect("SQLTable.db")
cuRsor = connection.cursor()

#SQL commands to create table in the database
sql_command = """CREATE TABLE employee_info(
                serial_number NUMBER(3),
                first_name VARCHAR(20),
                last_name VARCHAR(25),
                age NUMBER(2),
                gender CHAR(1) ); """
cuRsor.execute(sql_command)

#SQL command to insert an entry into the database
sql_command = """INSERT INTO employee_info VALUES (01, 'Tejshree', 'Lavatre', 20, 'F'), 
                (04, 'Prachi', 'Lavatre', 15, 'F'); """

cuRsor.execute(sql_command)

connection.commit()

connection.close()
