# Deleting a student record

import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="college"
)

cursor = connection.cursor()

delete_query = "DELETE FROM students WHERE id = %s"

student_id = 1

cursor.execute(delete_query, (student_id,))

connection.commit()

if cursor.rowcount > 0:
    print("Student deleted successfully.")
else:
    print("Student not found.")

cursor.close()
connection.close()