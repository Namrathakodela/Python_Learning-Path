# Working with CSV files

import csv

students = [
    ["Name", "Age", "Course"],
    ["Anu", 20, "CSE"],
    ["Ravi", 21, "ECE"],
    ["Priya", 20, "IT"]
]

with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(students)

print("CSV file created successfully.")

print("\nStudent Details:")

with open("students.csv", "r") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)