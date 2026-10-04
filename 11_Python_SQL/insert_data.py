# Inserting records into MySQL

import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="college"
)

cursor = connection.cursor()

insert_query = """
INSERT INTO students (name, age, course, marks)
VALUES (%s, %s, %s, %s)
"""

student = ("Anu", 20, "CSE", 85.5)

cursor.execute(insert_query, student)

connection.commit()

print("Student inserted successfully.")
print("Student ID:", cursor.lastrowid)

cursor.close()
connection.close()