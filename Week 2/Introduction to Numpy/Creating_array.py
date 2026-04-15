import numpy as np

array = np.array([1, 2, 3, 4])
print(f"Array:{array}")

zeroes = np.zeros((3, 3))
print(f"Zeros array:\n{zeroes}")

ones = np.ones((2, 4))
print(f"Ones array:\n{ones}")

range_array = np.arange(1, 100, 2)
print(f"Range array:\n{range_array}")

linspace_array = np.linspace(0, 1, 5)
print(f"Linspace array:{linspace_array}")
