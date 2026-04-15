# add = lambda x,y: x+y
# print(add(3,5))
# divide = lambda x,y:x-y
# print(divide(9,5))

from functools import reduce
numbers = [1, 2, 3, 4]
# map(): Applies a function to each item in an iterable
squares = map(lambda x: x ** 2, numbers)
print(list(squares))
# filter(): Filter items based on a condition
evenList = filter(lambda x: x % 2 == 0, numbers)
print(list(evenList))

# reduce() : Reduces an iterable to a single value
product = reduce(lambda x, y: x*y, numbers)
print(product)
