import pandas as pd
from scipy.stats import ttest_ind

# Load Dataset
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"
df = pd.read_csv(url)

# Seperate data by gender
male_tips = df[df['sex'] == 'Male']['tip']
female_tips = df[df['sex'] == 'Female']['tip']

# Perform t-test
t_stat, p_value = ttest_ind(male_tips, female_tips)
print("T-Statistic: ", t_stat)
print("P-Value: ", p_value)

# Interpret results
alpha = 0.05
if p_value < alpha:
    print("Reject all null hypothesis: Significant difference.")
else:
    print("Reject all null hypothesis: NO Significant difference.")
