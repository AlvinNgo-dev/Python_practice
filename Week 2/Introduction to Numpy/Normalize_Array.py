import numpy as np
# x′: Normalized array
# x′= (max(x)−min(x))/(x−min(x))​


def min_max_normalize(arr):
    arr = np.array(arr, dtype=float)
    min_val = arr.min()
    max_val = arr.max()

    if max_val == min_val:
        raise ValueError("Cannot normalize: all values are the same.")

    return (arr - min_val) / (max_val - min_val)


# Example
a = np.array([10, 20, 30, 40, 50])
normalized = min_max_normalize(a)
print(normalized)
