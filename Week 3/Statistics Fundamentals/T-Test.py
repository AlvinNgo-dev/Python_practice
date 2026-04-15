from scipy. stats import ttest_ind
import numpy as np
import random

# Sample Datasets
group1 = np.random.choice(np.arange(0, 3, 0.1), size=5)
group2 = np.random.choice(np.arange(0, 3, 0.1), size=5)

# Perform t-test
t_stat, p_value = ttest_ind(group1, group2)
print("T-Statistic: ", t_stat)
print("P-Value: ", p_value)

# Interpretation
alpha = 0.05
if p_value < alpha:
    print("Reject the null hypothesis: significant difference")
else:
    print("Failed to reject the null hypothesis: No significant difference")
