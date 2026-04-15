import numpy as np

# Random variable: dice roll
outcomes = np.array([1, 2, 3, 4, 5, 6])
probabilities = np.array([1/6] * 6)

# Expectation
expectation = np.sum(outcomes * probabilities)
print("Expectation (Mean): ", expectation)

# Variance and Standard Deviation
variance = np.sum((outcomes - expectation) ** 2 * probabilities)
# variance = np.var(outcomes)
std_dev = np.sqrt(variance)
# std_dev = np.std(outcomes)
print("Variance: ", variance)
print("Standard Deviation: ", std_dev)
