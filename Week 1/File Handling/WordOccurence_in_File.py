def word_counts(file_name):
    try:
        with open(file_name, "r") as file:
            count = 0
            word = str(input("Insert a word: "))
            for line in file:
                words = line.split()
                for w in words:
                    if w == word:
                        count += 1
            print(f"Total {word} found: {count}")
    except FileNotFoundError:
        print(f"File {file_name} not found!")


file_name = input("Enter file path:")
word_counts(file_name)
