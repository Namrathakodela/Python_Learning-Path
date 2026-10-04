# Searching for students

import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="college"
)

cursor = connection.cursor()

name = input("Enter student name: ")

search_query = """
SELECT * FROM students
WHERE name LIKE %s
"""

cursor.execute(search_query, (f"%{name}%",))

students = cursor.fetchall()

if students:
    print("\nSearch Results:")

    for student in students:
        print(
            "ID:", student[0],
            "| Name:", student[1],
            "| Age:", student[2],
            "| Course:", student[3],
            "| Marks:", student[4]
        )
else:
    print("No students found.")

cursor.close()
connection.close()