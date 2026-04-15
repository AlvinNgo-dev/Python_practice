# Take input from the user and convert it into an integer
num = int(input("Enter a number: "))

# Prime numbers must be greater than 1
if num > 1:

    # Assume the number is prime at the start
    is_prime = True

    # Loop from 2 to the square root of the number
    # If a number has a factor greater than its square root,
    # it must also have one smaller than the square root
    for i in range(2, int(num ** 0.5) + 1):

        # Check if num is divisible by i
        if num % i == 0:
            # If divisible, it is not a prime number
            is_prime = False
            break  # Exit the loop since we found a factor

    # After the loop, check the flag
    if is_prime:
        print(f"{num} is a prime number")
    else:
        print(f"{num} is not a prime number")

# If the number is 1 or less, it is not prime
else:
    print(f"{num} is not a prime number")
