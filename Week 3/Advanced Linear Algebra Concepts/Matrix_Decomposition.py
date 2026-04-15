import numpy as np
import random
A = np.random.randint(-3, 3, size=(3, 3))
print(f"Matrix A:\n{A}")

U, S, Vt = np.linalg.svd(A)
print("U: \n", U)
print("Singular Values: \n", S)
print("V Transpose: \n", Vt)

# Reconstruct
Sigma = np.zeros((3, 3))
np.fill_diagonal(Sigma, S)
reconstructed = U @ Sigma @ Vt
print("Reconstructed Matrix \n", np.round(reconstructed, 2))
