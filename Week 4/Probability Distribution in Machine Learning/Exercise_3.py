# Explore dataset with real wolrd applications of distributions

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import skew, kurtosis

np.random.seed(0)

# Simulated real-world datasets

# Human heights (Normal distribution)
heights = np.random.normal(loc=170, scale=10, size=1000)

# Customer arrival times (Exponential)
arrival_times = np.random.exponential(scale=5, size=1000)

# Number of calls per minute (Poisson)
calls = np.random.poisson(lam=4, size=1000)

# Income distribution (Log-normal)
income = np.random.lognormal(mean=10, sigma=0.5, size=1000)

datasets = {
    "Heights": heights,
    "Arrival Times": arrival_times,
    "Calls per Minute": calls,
    "Income": income
}

# Summary statistics
summary = []

for name, data in datasets.items():
    summary.append([
        name,
        np.mean(data),
        np.std(data),
        skew(data),
        kurtosis(data)
    ])

df = pd.DataFrame(summary, columns=[
    "Dataset", "Mean", "StdDev", "Skewness", "Kurtosis"
])

print(df)

plt.figure(figsize=(12, 8))

for i, (name, data) in enumerate(datasets.items()):
    plt.subplot(2, 2, i+1)
    sns.histplot(data, kde=True)
    plt.title(name)

plt.tight_layout()
plt.show()
