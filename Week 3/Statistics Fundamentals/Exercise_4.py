import numpy as np
from scipy import stats

# Data
n = 500        # total sample size
successes = 320

# Sample proportion
p_hat = successes / n

# Z-score for 95% confidence
z = stats.norm.ppf(0.975)

# Standard error
standard_error = np.sqrt((p_hat * (1 - p_hat)) / n)

# Confidence interval
margin_of_error = z * standard_error
lower_bound = p_hat - margin_of_error
upper_bound = p_hat + margin_of_error

print("Sample Proportion:", p_hat)
print("95% Confidence Interval:", round(
    lower_bound, 2), '--', round(upper_bound, 2))
