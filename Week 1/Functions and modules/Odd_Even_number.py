def even_num(a):
    if a % 2 == 0:
        return True
    else:
        return False


def Even_number_detector():
    num = int(input("Eneter a number:"))
    if even_num(num):
        print(f"{num} is an even number")
    else:
        print(f"{num} is an odd numer")


result = Even_number_detector()
