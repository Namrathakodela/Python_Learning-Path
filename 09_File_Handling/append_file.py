# Appending data to a file

file = open("output.txt", "a")

file.write("\nThis line was added later.")
file.write("\nPython makes file handling simple.")

file.close()

print("Data appended successfully.")