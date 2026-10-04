# Handling multiple exceptions

try:
    first_number = int(input("Enter first number: "))
    second_number = int(input("Enter second number: "))

    result = first_number / second_number
    print("Result:", result)

except ValueError:
    print("Invalid input. Please enter numbers only.")

except ZeroDivisionError:
    print("Cannot divide by zero.")

except Exception as error:
    print("An unexpected error occurred:", error)