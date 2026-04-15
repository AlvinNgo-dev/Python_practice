sentence = input("Enter a Sentence: ")

# Split the sentence into words
words = sentence.split()

# Initialize Dictionary
word_count = {}

# Count word frequence
for word in words:
    word = word. lower()
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
for key, value in word_count.items():
    print(f"{key}: {value}")
