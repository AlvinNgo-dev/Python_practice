# real_dataset_scipy_anova.py

import pandas as pd
import seaborn as sns
import numpy as np
from scipy import stats

# Load dataset
tips = sns.load_dataset("tips")

# We'll analyze tip amount by sex and day
df = tips[["tip", "sex", "day"]]

factor1 = "sex"
factor2 = "day"
response = "tip"

levels1 = df[factor1].unique()
levels2 = df[factor2].unique()

grand_mean = df[response].mean()

# Sum of squares for factor1
ss_factor1 = sum(
    len(df[df[factor1] == l]) *
    (df[df[factor1] == l][response].mean() - grand_mean) ** 2
    for l in levels1
)

# Sum of squares for factor2
ss_factor2 = sum(
    len(df[df[factor2] == l]) *
    (df[df[factor2] == l][response].mean() - grand_mean) ** 2
    for l in levels2
)

# Interaction SS
ss_interaction = 0
for l1 in levels1:
    for l2 in levels2:
        cell = df[(df[factor1] == l1) & (df[factor2] == l2)][response]
        if len(cell) > 0:
            ss_interaction += len(cell) * (
                cell.mean()
                - df[df[factor1] == l1][response].mean()
                - df[df[factor2] == l2][response].mean()
                + grand_mean
            ) ** 2

ss_total = sum((df[response] - grand_mean) ** 2)
ss_error = ss_total - ss_factor1 - ss_factor2 - ss_interaction

# Degrees of freedom
df1 = len(levels1) - 1
df2 = len(levels2) - 1
df_interaction = df1 * df2
df_error = len(df) - len(levels1)*len(levels2)

# Mean squares
ms1 = ss_factor1 / df1
ms2 = ss_factor2 / df2
ms_inter = ss_interaction / df_interaction
ms_error = ss_error / df_error

# F statistics
F1 = ms1 / ms_error
F2 = ms2 / ms_error
F_inter = ms_inter / ms_error

# p-values
p1 = stats.f.sf(F1, df1, df_error)
p2 = stats.f.sf(F2, df2, df_error)
p_inter = stats.f.sf(F_inter, df_interaction, df_error)

print("Two-Way ANOVA (SciPy) on Tips Dataset\n")

print(f"{factor1} effect: F={F1:.3f}, p={p1:.5f}")
print(f"{factor2} effect: F={F2:.3f}, p={p2:.5f}")
print(f"Interaction: F={F_inter:.3f}, p={p_inter:.5f}")
