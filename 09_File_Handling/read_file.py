# Reading a file in Python

file = open("sample.txt", "r")

content = file.read()

print("File content:")
print(content)

file.close()