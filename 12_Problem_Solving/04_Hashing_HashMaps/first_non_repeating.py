# First Non-Repeating Element

values = [4, 5, 1, 2, 1, 4, 5]

frequency = {}

for value in values:
    frequency[value] = frequency.get(value, 0) + 1

for value in values:

    if frequency[value] == 1:
        print("First non-repeating element:", value)
        break