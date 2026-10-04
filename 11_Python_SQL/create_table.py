# Creating a database and table using Python

import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password"
)

cursor = connection.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS college")

cursor.execute("USE college")

create_table_query = """
CREATE TABLE IF NOT EXISTS students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    age INT,
    course VARCHAR(100),
    marks FLOAT
)
"""

cursor.execute(create_table_query)

print("Database and table created successfully.")

cursor.close()
connection.close()