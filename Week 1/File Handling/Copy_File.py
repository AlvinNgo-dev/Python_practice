def copy_file(file_name1, file_name2):
    try:
        with open(file_name1, "r") as file:
            content = file.readlines()
    except FileNotFoundError:
        print(f"File name {file_name1} not found!")

    try:
        with open(file_name2, "w") as file:
            for item in content:
                file.write(item)
    except FileExistsError:
        print(f"File {file_name2} already exist!")


file_name1 = input("Enter file path to copy:")
file_name2 = input("Enter file path to paste:")
copy_file(file_name1, file_name2)
