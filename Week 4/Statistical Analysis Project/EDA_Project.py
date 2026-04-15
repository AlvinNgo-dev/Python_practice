# url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load Dataset
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"
df = pd.read_csv(url)

del df["sex"]
del df["smoker"]
del df["day"]
del df["time"]

# Inspect Data
print(df.info())
print(df.describe())

# Visualize Distributions
sns.histplot(df["total_bill"], kde=True)
plt.title("Distribution of Total Bill")
plt.show()

# Correlation heatmap
sns.heatmap(df.corr(), annot=True, cmap="coolwarm")
plt.title("Cofrelation Heatmap")
plt. show()
