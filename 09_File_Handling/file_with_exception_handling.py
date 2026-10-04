# File handling with exception handling

try:
    file = open("sample.txt", "r")

    content = file.read()

    print("File content:")
    print(content)

except FileNotFoundError:
    print("The file was not found.")

except PermissionError:
    print("You do not have permission to access this file.")

finally:
    try:
        file.close()
    except NameError:
        pass

    print("File operation completed.")