import numpy as np
import random

A = np.random.randint(0, 10, size=(2, 2))
B = np.random.randint(0, 10, size=(2, 2))
print("Matrix A:\n", A)
# print("Matrix B:\n", B)
# print(f"Addition: \n{A+B}")
# print(f"Subtraction: \n{A-B}")

C = 2 * A
print("Scalar Multiplication: \n", C)

result = np.dot(A, C)
print("Matrix Multiplication \n", result)
