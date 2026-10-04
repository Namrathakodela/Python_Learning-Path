# Find Duplicate Elements using Hash Set

numbers = [1, 2, 3, 2, 4, 5, 3, 6]

seen = set()
duplicates = set()

for number in numbers:

    if number in seen:
        duplicates.add(number)
    else:
        seen.add(number)

print("Duplicate elements:", duplicates)