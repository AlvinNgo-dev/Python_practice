import numpy as np
import random
from statistics import mode
data = np.random.choice(np.arange(10, 100, 10), size=10)
mean = sum(data) / len(data)
print(f"Data: {data}")
print(f"Mean: {mean}")

sorted_data = sorted(data)
median = sorted_data[len(data) // 2] if len(data) % 2 != 0 else \
    (sorted_data[len(data) // 2 - 1] + sorted_data[len(data) // 2]) / 2
print("Median: ", median)

print(f"Mode: {mode(data)}")

variance = sum((x - mean) ** 2 for x in data) / len(data)
print("Variance: ", variance)

std_dev = variance ** 0.5
print("Standard Deviation:", std_dev)
