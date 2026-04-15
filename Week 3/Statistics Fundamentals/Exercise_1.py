import numpy as np
import random
import scipy.stats as stats
from statistics import mode
data = np.random.choice(np.arange(10, 50, 10), size=5)
mean = np.mean(data)
variance = np.var(data)
std_dev = np.std(data)

print(data)
print(f"Mean: {mean}")
print(f"Variance: {variance}")
print(f"Standard deviation: {std_dev}")
print(f"Mode: {mode(data)}")
