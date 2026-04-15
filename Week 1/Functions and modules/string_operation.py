def string_reverse(string):
    reversed_string = string[::-1]
    return reversed_string


def count_vowels(string):
    vowels = "aeiouAEIOU"
    vowel_list = [c for c in string if c in vowels]
    return len(vowel_list), vowel_list


def is_palindrome(string):
    s = string.lower()
    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True
