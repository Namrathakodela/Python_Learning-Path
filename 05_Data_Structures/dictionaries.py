# Python Dictionaries

student = {
    "name": "Namratha",
    "age": 21,
    "branch": "CSE",
    "college": "BTech"
}

print("Student:", student)

# Accessing values
print("Name:", student["name"])
print("Age:", student["age"])

# Using get()
print("Branch:", student.get("branch"))

# Adding a new key
student["city"] = "Hyderabad"

print("After adding city:", student)

# Updating
student["age"] = 22

print("After updating age:", student)

# Removing
student.pop("city")

print("After removing city:", student)

# Keys
print("Keys:", student.keys())

# Values
print("Values:", student.values())

# Items
print("Items:", student.items())

# Looping
for key, value in student.items():
    print(key, ":", value)