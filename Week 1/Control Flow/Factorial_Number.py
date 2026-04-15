def factorial_number(a):
    if a < 0:
        return "Factorial is not defined for negative numbers"

    n = 1
    if a == 0 or a == 1:
        return 1
    else:
        for i in range(a, 0, -1):
            n *= i
    return n


while True:
    number = int(input("Enter a number: "))
    print(f"The factorial number of {number} is {factorial_number(number)}")
    text = str(input("Press q to exit or Enter to continue! "))
    if text != 'q':
        continue
    else:
        break
