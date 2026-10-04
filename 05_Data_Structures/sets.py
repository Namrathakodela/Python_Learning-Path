# Python Sets

numbers = {1, 2, 3, 4, 5}

print("Original set:", numbers)

# Adding
numbers.add(6)
print("After add:", numbers)

# Adding multiple elements
numbers.update([7, 8, 9])
print("After update:", numbers)

# Removing
numbers.remove(3)
print("After remove:", numbers)

# Discard
numbers.discard(10)

# Set operations
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

print("Union:", set_a.union(set_b))
print("Intersection:", set_a.intersection(set_b))
print("Difference:", set_a.difference(set_b))
print("Symmetric Difference:",
      set_a.symmetric_difference(set_b))

# Remove duplicates from a list
values = [1, 2, 2, 3, 3, 4, 5, 5]

unique_values = set(values)

print("Unique values:", unique_values)