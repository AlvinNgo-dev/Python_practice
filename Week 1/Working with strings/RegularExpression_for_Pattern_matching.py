import re  # Import the regular expressions module

text = "Contact me at 123-456-7890"  # The input string containing a phone number

# Search for a phone number pattern: 3 digits - 3 digits - 4 digits
number = re.search(r"\d{3}-\d{3}-\d{4}", text)
print(number.group())  # Print the matched phone number

# Find all groups of one or more digits in the text
digits = re.findall(r"\d+", text)
print(digits)  # Print all digit sequences as a list

# Replace every digit in the text with the letter 'X'
updated_text = re.sub(r"\d", "X", text)
print(updated_text)  # Print the masked version of the text
