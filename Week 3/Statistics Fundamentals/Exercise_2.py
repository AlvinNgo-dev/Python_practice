import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Generate sample data
data = np.random.choice(np.arange(10, 100, 10), size=100)

# Calculate statistics
mean_value = np.mean(data)
median_value = np.median(data)
mode_result = stats.mode(data, keepdims=True)
mode_value = mode_result.mode[0]   # extract scalar

# Plot histogram
plt.figure()
plt.hist(data, bins=len(np.unique(data)))

plt.axvline(mean_value, linestyle='solid',
            linewidth=2, color='red', label='Mean')
plt.axvline(median_value, linestyle='dashed',
            linewidth=2, color='blue', label='Median')
plt.axvline(mode_value, linestyle='dotted',
            linewidth=2, color='green', label='Mode')

plt.legend()
plt.show()

print("Mean:", mean_value)
print("Median:", median_value)
print("Mode:", mode_value)
