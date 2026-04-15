import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])

evens = arr[arr % 2 == 0]
print("Evens: ", evens)

arr[arr > 3] = 0
print("Modified Array: ", arr)
