# Using raise to manually create an exception

def check_age(age):
    if age < 18:
        raise ValueError("Age must be 18 or above.")

    print("You are eligible.")

try:
    age = int(input("Enter your age: "))
    check_age(age)

except ValueError as error:
    print("Error:", error)