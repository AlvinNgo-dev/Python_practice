# List structure
numbers = [1, 2, 3, 4]

fruits = ["apple", "banana", "cherry"]

mixed = [1, "apple", True]

print(numbers[3])
print(fruits[0])
print(mixed[1])

fruits.append("pearl")
fruits.insert(1, "orange")
fruits.remove("cherry")
del fruits[0]
fruits.pop()
print(fruits)
