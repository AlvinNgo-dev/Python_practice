try:
    with open("Theory and Practices\File Handling\sample.txt", "r") as file:
        content = file.readline()
        print(content)
except FileNotFoundError:  # FileNotFoundError | PermissionError | IOError
    print("File Not Found!")
