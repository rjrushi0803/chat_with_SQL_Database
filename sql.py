import sqlite3

## connect to sqlite
connection = sqlite3.connect("student.db")

## create a cursor which will help in insert, record, create table, retrive
cursor = connection.cursor()

## create the table
table_info = '''
CREATE TABLE new_student(name VARCHAR(25),
class VARCHAR(25),
section VARCHAR,
marks INT)
'''

## to create table we need to execute above querry which in the string format
cursor.execute(table_info)

## inserting some values in table

values = '''
INSERT INTO new_student VALUES('Abhishek', 'Data science','A',90),
('Avishkar','Data science', 'B', 100),
('Mahesh','Data science','A',86),
('Nilesh','Data science','B',75),
('Rushi','Data science','A',35)
'''

cursor.execute(values)

## dispaly all the records
print('student Database')

data=cursor.execute('''SELECT * FROM new_student''')

for row in data:
    print(row)

## close the connection
connection.commit()
connection.close()
