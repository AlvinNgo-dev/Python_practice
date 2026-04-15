import numpy as np
from scipy import stats

# Sample data: exam scores from two groups
group_A = np.array([78, 85, 82, 88, 90, 79, 84])
group_B = np.array([72, 75, 70, 68, 74, 73, 71])

# Perform independent t-test
t_statistic, p_value = stats.ttest_ind(group_A, group_B)

print("T-statistic:", t_statistic)
print("P-value:", p_value)

# Decision rule
alpha = 0.05
if p_value < alpha:
    print("Reject the null hypothesis (significant difference).")
else:
    print("Fail to reject the null hypothesis (no significant difference).")
