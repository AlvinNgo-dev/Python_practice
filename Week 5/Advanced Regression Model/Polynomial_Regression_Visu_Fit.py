import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_california_housing
from sklearn.preprocessing import PolynomialFeatures
from sklearn. linear_model import LinearRegression, Ridge, Lasso
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

# Load the California Housing dataset
data = fetch_california_housing(as_frame=True)
df = data.frame
df.to_csv(r"Practice\Theory and Practices\Week 5\Advanced Regression Model\fetch_california_housing.csv", index=False)
# Select feature (Median Income) and traget (Median House Value)
X = df[['MedInc']]
y = df[['MedHouseVal']]

# Transfrom feature to Polynomial features
poly = PolynomialFeatures(degree=2, include_bias=False)
X_poly = poly.fit_transform(X)

# Fit Polynomial regresson model
model = LinearRegression()
model.fit(X_poly, y)

# Make prediction
y_pred = model.predict(X_poly)

# Plot Actual vs Predicted values
plt.figure(figsize=(10, 6))
plt.scatter(X, y, color="blue", label="Actual data", alpha=0.5)
plt.plot(X, y_pred, color="red", label="Predicted curve", alpha=0.5)
plt.title("Polynomial Regression")
plt.xlabel("Median Income in California")
plt.ylabel("Median House Value in California")
plt.legend()
plt.show()

# Evaluate model performance
mse = mean_squared_error(y, y_pred)
rmse = np.sqrt(mse)
print("MSE:", mse)
