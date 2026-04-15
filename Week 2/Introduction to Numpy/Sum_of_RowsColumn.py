import numpy as np


def sum_rows_and_columns(array):
    columns = 0
    rows = 0
    for i in range(a.shape[0]):
        rows += 1
    for j in range(a.shape[1]):
        columns += 1
    print(f"Rows: {rows}")
    print(f"Columns: {columns}")
    return columns + rows


a = np.array([[1, 2, 3],
              [4, 5, 6]])
print(sum_rows_and_columns(a))
