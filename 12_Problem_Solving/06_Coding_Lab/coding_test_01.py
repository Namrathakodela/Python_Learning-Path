# Coding Lab Test 01
# Problem: Find the first non-repeating character in a string

def first_non_repeating_character(text):

    frequency = {}

    # Count frequency of each character
    for char in text:
        if char != " ":
            frequency[char] = frequency.get(char, 0) + 1

    # Find first character with frequency 1
    for char in text:
        if char != " " and frequency[char] == 1:
            return char

    return None


text = input("Enter a string: ")

result = first_non_repeating_character(text)

if result:
    print("First non-repeating character:", result)
else:
    print("No non-repeating character found.")