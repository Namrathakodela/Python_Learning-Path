# String Problems

# 1. Reverse a string

text = "Python"

reverse = text[::-1]

print("Original:", text)
print("Reversed:", reverse)


# 2. Check palindrome

word = input("Enter a word: ")

if word.lower() == word.lower()[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")


# 3. Count vowels

text = input("Enter a string: ")

vowels = "aeiou"
count = 0

for character in text.lower():
    if character in vowels:
        count += 1

print("Number of vowels:", count)


# 4. Count characters

text = input("Enter a string: ")

frequency = {}

for character in text:
    if character != " ":
        frequency[character] = frequency.get(character, 0) + 1

print("Character frequency:", frequency)


# 5. Remove spaces

text = input("Enter a string: ")

result = text.replace(" ", "")

print("Without spaces:", result)