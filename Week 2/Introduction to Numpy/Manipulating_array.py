import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
reshaped = arr. reshape((3, 3))
print(reshaped)

arr = np.array([1, 2, 3])
expanded = arr[:, np.newaxis]  # Turn any array into 1 collumn
print(expanded)
