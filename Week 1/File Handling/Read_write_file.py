# with Statement: Ensures files are properly closed after operations, even if an exception occurs
with open("D:\Python Practice\Practice\Theory and Practices\File Handling\sample.txt", "r") as file:  # r|w|a|r+
    content = file. readlines()         # read()|readline()|readlines()
    print(content)
    # file.write("Hello, World!")
    # file.writelines(["Alice", "Bob", "Cherry"])  # write()|writelines()
