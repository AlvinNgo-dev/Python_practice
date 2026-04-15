from scipy.stats import f_oneway

# Data for three groups
group1 = [12, 14, 15, 16, 17]
group2 = [11, 13, 14, 15, 16]
group3 = [10, 12, 13, 14, 15]

# Perform ANOVA
f_stat, p_value = f_oneway(group1, group2, group3)
print("F-Statistic: ", f_stat)
print("P-Value: ", p_value)
