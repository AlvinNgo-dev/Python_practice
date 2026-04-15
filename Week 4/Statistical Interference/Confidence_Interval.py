import numpy as np
from scipy.stats import norm

# Sample Data
data = np.random.normal(loc=50, scale=10, size=100)

# Calculate mean and standard deviation
mean = np.mean(data)
std = np.std(data, ddof=1)

# 95% Confidence Interval (using t-distribution)
n = len(data)
z_value = norm.ppf(0.975)
margin_of_error = z_value * (std / np.sqrt(n))
ci = np.round((mean - margin_of_error, mean + margin_of_error), 3)

print("Sample: ", mean)
print("95% COnfidence Interval: ", ci)
