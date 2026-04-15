# Write a program to reverse a list and remove duplicates using a set
def reverse_and_remove_duplicates(lst):
    seen = set()
    result = []

    # Traverse the list in reverse order
    for item in reversed(lst):
        if item not in seen:
            seen.add(item)
            result.append(item)

    return result


# Example
lst = ["apple", "banana", "apple", "cherry", "banana"]

output = reverse_and_remove_duplicates(lst)
print(output)
