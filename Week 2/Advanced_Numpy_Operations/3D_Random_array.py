import numpy as np

matrix = np.random.randint(0, 101, size=(3, 3, 3))
print(matrix)

# calculate summary stats
print("Sum: ", np.sum(matrix))
print("Mean: ", np.mean(matrix))
print("Standard Deviation: ", np.std(matrix))
