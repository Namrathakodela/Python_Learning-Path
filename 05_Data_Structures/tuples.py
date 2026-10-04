# Python Tuples

colors = ("red", "green", "blue", "yellow")

print("Tuple:", colors)

# Accessing elements
print("First:", colors[0])
print("Last:", colors[-1])

# Length
print("Length:", len(colors))

# Checking an element
print("green" in colors)

# Counting elements
numbers = (1, 2, 3, 2, 4, 2, 5)

print("Count of 2:", numbers.count(2))

# Finding index
print("Index of 3:", numbers.index(3))

# Looping
for color in colors:
    print(color)