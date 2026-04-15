def largest_number(a):
    numbers = []
    for i in range(n):
        num = int(input("Enter number: "))
        numbers.append(num)
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest


n = int(input("Define amount of numbers in a list: "))
print("Largest number in the list is: ", largest_number(n))
