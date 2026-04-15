import numpy as np

# outcomes of the die
faces = np.array([1, 2, 3, 4, 5, 6])

# probabilities (must sum to 1)
probs = np.array([0.05, 0.10, 0.15, 0.20, 0.25, 0.25])

# simulate rolls
n = 1000000
rolls = np.random.choice(faces, size=n, p=probs)

# expectation estimate
expectation = np.mean(rolls)

# variance estimate
variance = np.var(rolls)

print("Estimated E[X]:", expectation)
print("Estimated Var(X):", variance)
