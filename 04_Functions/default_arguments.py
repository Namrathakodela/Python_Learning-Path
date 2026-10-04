# Default Arguments

def greet(name="User"):
    print("Hello", name)


greet()
greet("Namratha")


def calculate_bill(amount, tax=5):
    total = amount + (amount * tax / 100)
    return total


print("Total bill:", calculate_bill(1000))
print("Total bill:", calculate_bill(1000, 10))