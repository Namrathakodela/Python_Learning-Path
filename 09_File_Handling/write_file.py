# Writing data to a file

file = open("output.txt", "w")

file.write("Hello, Python!\n")
file.write("I am learning file handling.\n")
file.write("This file was created using Python.")

file.close()

print("Data written successfully.")