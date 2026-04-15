import re


def vowel_counter(text):
    # Remove punctuation
    text = re.sub(r"[^\w\s]", "", text)
    # Remove extra spaces
    text = " ".join(text.split())
    # Convert to lowercase
    text = text. lower()
    seen = "aeiyou"
    count = 0
    for i in text:
        if i in seen:
            count += 1
    return count


input_text = ("Hello, World. !!! Welcome to Python, Programming ....")
print(vowel_counter(input_text))
