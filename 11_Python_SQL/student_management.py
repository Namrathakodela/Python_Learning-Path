# Student Management System using Python and MySQL

import mysql.connector


def create_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="your_password",
        database="college"
    )


def add_student():
    connection = create_connection()
    cursor = connection.cursor()

    name = input("Enter name: ")
    age = int(input("Enter age: "))
    course = input("Enter course: ")
    marks = float(input("Enter marks: "))

    query = """
    INSERT INTO students (name, age, course, marks)
    VALUES (%s, %s, %s, %s)
    """

    cursor.execute(query, (name, age, course, marks))

    connection.commit()

    print("Student added successfully.")

    cursor.close()
    connection.close()


def view_students():
    connection = create_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM students")

    students = cursor.fetchall()

    print("\nStudent Records")
    print("-" * 60)

    for student in students:
        print(
            f"ID: {student[0]} | "
            f"Name: {student[1]} | "
            f"Age: {student[2]} | "
            f"Course: {student[3]} | "
            f"Marks: {student[4]}"
        )

    cursor.close()
    connection.close()


def update_student():
    connection = create_connection()
    cursor = connection.cursor()

    student_id = int(input("Enter student ID: "))
    marks = float(input("Enter new marks: "))

    query = """
    UPDATE students
    SET marks = %s
    WHERE id = %s
    """

    cursor.execute(query, (marks, student_id))

    connection.commit()

    if cursor.rowcount > 0:
        print("Student updated successfully.")
    else:
        print("Student not found.")

    cursor.close()
    connection.close()


def delete_student():
    connection = create_connection()
    cursor = connection.cursor()

    student_id = int(input("Enter student ID: "))

    query = "DELETE FROM students WHERE id = %s"

    cursor.execute(query, (student_id,))

    connection.commit()

    if cursor.rowcount > 0:
        print("Student deleted successfully.")
    else:
        print("Student not found.")

    cursor.close()
    connection.close()


while True:

    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    try:
        if choice == "1":
            add_student()

        elif choice == "2":
            view_students()

        elif choice == "3":
            update_student()

        elif choice == "4":
            delete_student()

        elif choice == "5":
            print("Exiting program...")
            break

        else:
            print("Invalid choice.")

    except ValueError:
        print("Please enter valid numerical values.")

    except mysql.connector.Error as error:
        print("Database error:", error)