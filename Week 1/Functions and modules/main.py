import string_operation as so

input_string = str(input("Enter a string or text:"))
result = so.count_vowels(input_string)
print(f"Reversed string: {so.string_reverse(input_string)}")
print(f"Vowels Counts: {result[0]}, Vowels found: {result[1]}")
print(f"Palindrome String: {so.is_palindrome(input_string)}")
