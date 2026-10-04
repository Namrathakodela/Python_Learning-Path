# Using finally

try:
    number = int(input("Enter a number: "))
    result = 100 / number
    print("Result:", result)

except ValueError:
    print("Invalid input.")

except ZeroDivisionError:
    print("Cannot divide by zero.")

finally:
    print("This block always executes.")