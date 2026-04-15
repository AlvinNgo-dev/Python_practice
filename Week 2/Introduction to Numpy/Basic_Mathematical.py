import numpy as np

a = np.arange(1, 6)
b = np.arange(6, 11)
print(a)
print(b)
print(f"Sum: {a+b}")
print(f"Divde: {a-b}")
print(f"Multiply: {a*b}")
print(f"Divide: {a/b}")

matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Original Matrix: \n", matrix)

# Transpose
transpose = matrix.T
print("Transpose:\n", transpose)

another_matrix = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]])
print("Addition: \n", matrix + another_matrix)
print("Multiplication : \n", matrix * another_matrix)
