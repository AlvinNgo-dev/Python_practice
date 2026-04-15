import numpy as np
import random

A = np.random.randint(0, 10, size=(3, 3))
B = np.random.randint(0, 10, size=(3, 3))
C = np.random.randint(0, 10, size=(3, 3))
print(A)
I = np.eye(3)
print(I)
print(f"Matrix A * Matrix I = \n{np.dot(A, I)}")

# Diagboal and Zero Matrix
D = np.diag([1, 7, 9])
Z = np.zeros((3, 3))
print("Diagonal Matrix\n", D)
print("Zero Matrix\n", Z)

det_A = np.linalg.det(A)
print(f"Determinant of matrix A:\n {det_A}")

inv_A = np.linalg.inv(A)
print(f"Inverse of matrix A:\n {inv_A}")

# Verify properties of matrix multiplication
print("Associative:", np.allclose((A@B)@C, A@(B@C)))
print("Distributive:", np.allclose(A@(B+C), A@B + A@C))
print("Identity:", np.allclose(A@I, A) and np.allclose(I@A, A))
print("Zero:", np.allclose(A@Z, Z) and np.allclose(Z@A, Z))
print("Transpose:", np.allclose((A@B).T, B.T@A.T))
print("Commutative (should be False):", np.allclose(A@B, B@A))
