import pandas as pd
import numpy as np
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error


# Load the dataset
data = pd.read_csv(
    r'Practice\Theory and Practices\Week 6\Creating and Transforming Features\bike_sharing_daily.csv'
)

# Display dataset information
print("Dataset Information:")
print(data.info())

# Preview the first few rows of the dataset
print("\nDataset Preview:")
print(data.head())

# Convert 'dteday' to datetime format
data['dteday'] = pd.to_datetime(data['dteday'])

# Create new features from 'dteday'
data['day_of_week'] = data['dteday'].dt.day_name()
data['month'] = data['dteday'].dt.month
data['year'] = data['dteday'].dt.year

# Display the new features
print("\nDataset with New Features:")
print(data[['dteday', 'day_of_week', 'month', 'year']].head())

# Select new freatures and target variable
X = data[['temp']]
y = data['cnt']

# Apply Polynomial Features transformation
poly = PolynomialFeatures(degree=2, include_bias=False)
X_poly = poly.fit_transform(X)

# Display the transformed features
print("\n Original and Polynomial Features:")
print(pd.DataFrame(X_poly, columns=['temp', 'temp^2']).head())

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X_poly, y, test_size=0.2, random_state=42)
X_poly_train, X_poly_test = train_test_split(
    X_poly, test_size=0.2, random_state=42)

# Train and evaluate model with original features
model_original = LinearRegression()
model_original.fit(X_train, y_train)
y_pred_original = model_original.predict(X_test)
mse_original = mean_squared_error(y_test, y_pred_original)

# Train and evaluate model with polynomial features
model_poly = LinearRegression()
model_poly.fit(X_poly_train, y_train)
y_pred_poly = model_poly.predict(X_poly_test)
mse_poly = mean_squared_error(y_test, y_pred_poly)

# Compare the performance of both models
print("\nMean Squared Error with Original Features:", round(mse_original, 2))
print("Mean Squared Error with Polynomial Features:", round(mse_poly, 2))
