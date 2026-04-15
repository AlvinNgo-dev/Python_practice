import numpy as np
# Generate random dataset
dataset = np.random.randint(0, 100, size=(5, 5))
print(f"Original dataset:\n{dataset}")

# Filter dataset and replace with 0 and 1 within threshold
dataset[dataset < 50] = 0
dataset[dataset >= 50] = 1
print(f"Binary mask dataset:\n{dataset}")
