# two_way_anova_scipy.py

import pandas as pd
import numpy as np
from scipy import stats

# Example dataset
data = {
    "Score": [85, 78, 92, 88, 76, 81, 95, 89, 72, 84, 90, 87],
    "Gender": ["Male", "Male", "Male", "Male", "Female", "Female", "Female", "Female", "Male", "Female", "Male", "Female"],
    "Class": ["A", "A", "B", "B", "A", "A", "B", "B", "A", "B", "A", "B"]
}

df = pd.DataFrame(data)

# Unique groups
genders = df["Gender"].unique()
classes = df["Class"].unique()

# Grand mean
grand_mean = df["Score"].mean()

# Sum of squares
ss_gender = sum(
    len(df[df["Gender"] == g]) *
    (df[df["Gender"] == g]["Score"].mean() - grand_mean) ** 2
    for g in genders
)

ss_class = sum(
    len(df[df["Class"] == c]) *
    (df[df["Class"] == c]["Score"].mean() - grand_mean) ** 2
    for c in classes
)

ss_interaction = 0
for g in genders:
    for c in classes:
        cell = df[(df["Gender"] == g) & (df["Class"] == c)]["Score"]
        if len(cell) > 0:
            cell_mean = cell.mean()
            ss_interaction += len(cell) * (
                cell_mean
                - df[df["Gender"] == g]["Score"].mean()
                - df[df["Class"] == c]["Score"].mean()
                + grand_mean
            ) ** 2

# Total SS
ss_total = sum((df["Score"] - grand_mean) ** 2)

# Error SS
ss_error = ss_total - ss_gender - ss_class - ss_interaction

# Degrees of freedom
df_gender = len(genders) - 1
df_class = len(classes) - 1
df_interaction = df_gender * df_class
df_error = len(df) - len(genders) * len(classes)

# Mean squares
ms_gender = ss_gender / df_gender
ms_class = ss_class / df_class
ms_interaction = ss_interaction / df_interaction
ms_error = ss_error / df_error

# F statistics
F_gender = ms_gender / ms_error
F_class = ms_class / ms_error
F_interaction = ms_interaction / ms_error

# p-values
p_gender = stats.f.sf(F_gender, df_gender, df_error)
p_class = stats.f.sf(F_class, df_class, df_error)
p_interaction = stats.f.sf(F_interaction, df_interaction, df_error)

print("Two-Way ANOVA Results (SciPy)\n")
print(f"Gender effect: F={F_gender:.3f}, p={p_gender:.4f}")
print(f"Class effect: F={F_class:.3f}, p={p_class:.4f}")
print(f"Interaction effect: F={F_interaction:.3f}, p={p_interaction:.4f}")
