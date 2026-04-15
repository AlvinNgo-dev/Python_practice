import numpy as np


def min_max(self):
    print(f"Maximum value in the array: {np.max(self)}")
    print(f"Minimum value in the array: {np.min(self)}")


a = np.random.rand(5)           # 1D array, length 5
print(f" First array:\n{a}")
print(min_max(a))
b = np.random.rand(3, 4)   # 2D array, shape (3, 4)
print(f"Second array:\n{b}")
print(min_max(b))
