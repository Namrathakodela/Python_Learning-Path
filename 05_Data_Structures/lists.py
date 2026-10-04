# Python Lists

fruits = ["apple", "banana", "orange", "mango"]

print("Original list:", fruits)

# Accessing elements
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])

# Adding elements
fruits.append("grapes")
print("After append:", fruits)

fruits.insert(1, "watermelon")
print("After insert:", fruits)

# Updating elements
fruits[0] = "pineapple"
print("After update:", fruits)

# Removing elements
fruits.remove("banana")
print("After remove:", fruits)

removed_item = fruits.pop()
print("Removed item:", removed_item)
print("After pop:", fruits)

# List length
print("Length:", len(fruits))

# Sorting
numbers = [5, 2, 8, 1, 9, 3]

numbers.sort()
print("Sorted:", numbers)

numbers.reverse()
print("Reversed:", numbers)

# Looping through a list
for fruit in fruits:
    print(fruit)