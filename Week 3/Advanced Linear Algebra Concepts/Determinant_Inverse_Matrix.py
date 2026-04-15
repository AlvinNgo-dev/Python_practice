import numpy as np

A = np.array([[2, 3], [1, 4]])
determinant = np. linalg.det(A)
print("Determinant: ", determinant)

inverse = np. linalg.inv(A)
print("Inverse of A: \n", inverse)
