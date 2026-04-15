import numpy as np
# Generate random dataset
dataset = np.random.randint(0, 100, size=(5, 5))
print(f"Original dataset: {dataset}")

# Filter dataset and replace with 0
dataset[dataset > 50] = 0
print(f"Modified dataset: {dataset}")

# calculate summary stats
print("Sum: ", np.sum(dataset))
print("Mean: ", np.mean(dataset))
print("Standard Deviation: ", np.std(dataset))
