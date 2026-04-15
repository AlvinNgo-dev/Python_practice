import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv(
    "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")
df = pd.DataFrame(data)

# Inspect data
print(df.info())
print(df.describe())

# Handle missing value
df["Age"] = df["Age"].fillna(df["Age"].median())
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])


# Remove duplicates
df = df.drop_duplicates()

# Filter data
first_class = df[df["Pclass"] == 1]
print("First Class Passengers: \n", first_class.head())

# Bar chart: Survival Rate by Class
survival_by_class = df.groupby("Pclass")["Survived"].mean()
survival_by_class.plot(kind="bar", color="green")
plt.title("Survival Rate by class")
plt.ylabel("Survival Rate")
# plt.show()

# Histogram: Age distribution
sns.histplot(df["Age"], kde=True, bins=20, color="purple")
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
# plt.show()

# Scatter Plot: Age vs Fare
plt.scatter(df["Age"], df["Fare"], alpha=0.5, color="skyblue")
plt.title("Age vs Fare")
plt.xlabel("Age")
plt.ylabel("Fare")
# plt.show()

# Multiple plot
plt.figure(figsize=(10, 14))

# Bar chart
plt.subplot(3, 1, 1)
survival_by_class.plot(kind="bar", color="green")
plt.title("Survival Rate by class")
plt.ylabel("Survival Rate")

# Histogram
plt.subplot(3, 1, 2)
sns.histplot(df["Age"], kde=True, bins=20, color="purple")
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")

# Scatter Plot
plt.subplot(3, 1, 3)
plt.scatter(df["Age"], df["Fare"], alpha=0.5, color="skyblue")
plt.title("Age vs Fare")
plt.xlabel("Age")
plt.ylabel("Fare")

# Adjust layout and show
plt.tight_layout()
plt.show()
