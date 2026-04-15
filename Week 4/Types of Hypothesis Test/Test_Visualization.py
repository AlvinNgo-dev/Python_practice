# visualization.py

import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
tips = sns.load_dataset("tips")

# Boxplot visualization
plt.figure(figsize=(8, 5))
sns.boxplot(x="day", y="tip", hue="sex", data=tips)

plt.title("Tip Distribution by Day and Gender")
plt.xlabel("Day")
plt.ylabel("Tip Amount")
plt.legend(title="Gender")

plt.show()

# Barplot visualization (mean values)
plt.figure(figsize=(8, 5))
sns.barplot(x="day", y="tip", hue="sex", data=tips)

plt.title("Average Tips by Day and Gender")
plt.xlabel("Day")
plt.ylabel("Average Tip")

plt.show()
