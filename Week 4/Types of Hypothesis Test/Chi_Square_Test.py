from scipy.stats import chi2_contingency

# Contingency Table
data = [[50, 30], [20, 40]]

# Perform Chi-Square Test
chi2, p, dof, expected = chi2_contingency(data)
print("Chi-Square Statistic: ", chi2)
print("P-Value: ", p)
print("Expected Frequencies: \n", expected)
