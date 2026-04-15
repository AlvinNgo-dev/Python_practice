# Task 1: Perform EDA and Preprocessing
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
# Load datasets
data = fetch_california_housing(as_frame=True)
df = data.frame
df.to_csv(r"D:\Python Practice\Practice\Theory and Practices\Week 5\Supervised Learning Mini Project\fetch_california_housing.csv", index=False)

X = df[['MedInc', 'AveRooms', 'HouseAge', ]]
y = df['MedHouseVal']


# Inspect data
print(df.info())
print(df.describe())

# Visualize relationships
sns.pairplot(df, vars=['MedInc', 'AveRooms', 'HouseAge', 'MedHouseVal'])
plt.show()

# Check for missing values
print("Missing values: \n", df.isnull().sum())

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

# Train Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate performance
mse = mean_squared_error(y_test, y_pred)
print("Linear Regression MSE:", mse)

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
