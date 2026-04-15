# Task 1: Perform EDA and Preprocessing
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_california_housing

# Load datasets
data = fetch_california_housing(as_frame=True)
df = data.frame
df.to_csv(r"D:\Python Practice\Practice\Theory and Practices\Week 5\Supervised Learning Mini Project\fetch_california_housing.csv", index=False)


# Inspect data
print(df.info())
print(df.describe())

# Visualize relationships
sns.pairplot(df, vars=['MedInc', 'AveRooms', 'HouseAge', 'MedHouseVal'])
plt.show()

# Check for missing values
print("Missing values: \n", df.isnull().sum())


# Load Telco Customer Churn Dataset
df_telco = pd.read_csv(
    'Practice\Theory and Practices\Week 5\Supervised Learning Mini Project\Telco-Customer-Churn.csv')

# Inspect Data
print(df_telco.info())
print(df_telco.describe())

# Visualize churn distribution
sns.countplot(x='Churn', data=df_telco)
plt.title("Churn distribution")
plt.show()

# Handle missing values
df_telco.fillna(df_telco.mean, inplace=True)
