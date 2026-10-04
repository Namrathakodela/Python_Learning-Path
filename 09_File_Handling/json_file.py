# Working with JSON files

import json

student = {
    "name": "Anu",
    "age": 20,
    "course": "Computer Science",
    "skills": ["Python", "SQL", "HTML"]
}

# Writing JSON data
with open("student.json", "w") as file:
    json.dump(student, file, indent=4)

print("JSON file created successfully.")

# Reading JSON data
with open("student.json", "r") as file:
    data = json.load(file)

print("\nStudent Details:")
print("Name:", data["name"])
print("Age:", data["age"])
print("Course:", data["course"])
print("Skills:", data["skills"])