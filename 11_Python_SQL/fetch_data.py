# Fetching records from MySQL

import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="college"
)

cursor = connection.cursor()

cursor.execute("SELECT * FROM students")

students = cursor.fetchall()

print("Student Records:")
print("-" * 50)

for student in students:
    print(
        "ID:", student[0],
        "| Name:", student[1],
        "| Age:", student[2],
        "| Course:", student[3],
        "| Marks:", student[4]
    )

cursor.close()
connection.close()