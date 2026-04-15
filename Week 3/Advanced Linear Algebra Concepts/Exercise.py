import numpy as np
import random
A = np.random.randint(-5, 5, size=(5, 5))
print(f"Matrix A:\n{A}")

U, S, Vt = np.linalg.svd(A)
print("U: \n", U)
print("Singular Values: \n", S)
print("V Transpose: \n", Vt)

eigenValues, eigneVectors = np. linalg.eig(A)
print("EigenVal\n", eigenValues)
print("EigenVectors\n", eigneVectors)

# Reconstruct
Sigma = np.zeros((5, 5))
np.fill_diagonal(Sigma, S)
reconstructed = U @ Sigma @ Vt
print("Reconstructed Matrix \n", np.round(reconstructed, 2))

# Verify Av = λv for first eigenpair
i = 0
v = eigneVectors[:, i]
lam = eigenValues[i]

left = A @ v
right = lam * v

print("Av:\n", left)
print("λv:\n", right)
print("Difference (should be ≈ 0):\n", np.round(left - right, 10))
