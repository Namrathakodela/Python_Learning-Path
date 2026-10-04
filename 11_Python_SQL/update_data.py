# Updating a student record

import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="college"
)

cursor = connection.cursor()

update_query = """
UPDATE students
SET marks = %s
WHERE id = %s
"""

new_marks = 92
student_id = 1

cursor.execute(update_query, (new_marks, student_id))

connection.commit()

if cursor.rowcount > 0:
    print("Student record updated successfully.")
else:
    print("Student not found.")

cursor.close()
connection.close()