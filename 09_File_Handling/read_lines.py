# Reading a file line by line

file = open("sample.txt", "r")

lines = file.readlines()

print("Lines in the file:")

for line in lines:
    print(line.strip())

file.close()