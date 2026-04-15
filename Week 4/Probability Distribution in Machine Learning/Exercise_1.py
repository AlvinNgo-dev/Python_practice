# Comparing Skewness, Kurtosis, and Outliers

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import skew, kurtosis

np.random.seed(42)

# 1 Normal distribution
normal_data = np.random.normal(loc=0, scale=1, size=1000)

# 2 Right skewed distribution
skewed_data = np.random.exponential(scale=1, size=1000)

# 3 Heavy tail distribution (high kurtosis)
heavy_tail = np.random.standard_t(df=2, size=1000)

# 4 Normal with outliers
data_with_outliers = np.random.normal(0, 1, 1000)
data_with_outliers = np.append(data_with_outliers, [8, 9, -7])

datasets = {
    "Normal": normal_data,
    "Right Skewed": skewed_data,
    "Heavy Tail": heavy_tail,
    "With Outliers": data_with_outliers
}


def count_outliers(data):
    Q1 = np.percentile(data, 25)
    Q3 = np.percentile(data, 75)
    IQR = Q3 - Q1

    lower = Q1 - 1.5*IQR
    upper = Q3 + 1.5*IQR

    return np.sum((data < lower) | (data > upper))


results = []

for name, data in datasets.items():

    s = skew(data)
    k = kurtosis(data)   # excess kurtosis
    out = count_outliers(data)

    results.append([name, s, k, out])

df = pd.DataFrame(results, columns=[
                  "Dataset", "Skewness", "Kurtosis", "Outliers"])
print(df)

# Visualization
plt.figure(figsize=(12, 8))

for i, (name, data) in enumerate(datasets.items()):
    plt.subplot(2, 2, i+1)
    plt.hist(data, bins=40)
    plt.title(name)

plt.tight_layout()
plt.show()
