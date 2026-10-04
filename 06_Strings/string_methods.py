# String Methods

text = "  Python Programming  "

print("Original:", text)

print("Upper:", text.upper())
print("Lower:", text.lower())
print("Title:", text.title())
print("Capitalized:", text.capitalize())

print("Stripped:", text.strip())

message = "Python is easy to learn"

print("Replace:", message.replace("easy", "powerful"))

print("Starts with Python:", message.startswith("Python"))
print("Ends with learn:", message.endswith("learn"))

print("Position of easy:", message.find("easy"))

# Split
words = message.split()

print("Words:", words)

# Join
joined = "-".join(words)

print("Joined:", joined)

# Count
print("Number of 'o':", message.count("o"))

# Checking content
print("Is alphabetic:", "Python".isalpha())
print("Is digit:", "12345".isdigit())