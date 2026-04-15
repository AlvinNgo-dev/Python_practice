import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

# Load data
path = r"Practice\Theory and Practices\Week 5\Supervised Learning and Regression Model\TCP_Log - Appearance Status.csv"
df = pd.read_csv(path)

# Features and target
X = df[["In Quantities"]]   # make it 2D
y = df["Out Quantities"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Coefficients
print("Slope:", model.coef_[0])
print("Intercept:", model.intercept_)

# Sort for clean plotting
sorted_idx = X_test["In Quantities"].argsort()
X_test_sorted = X_test.iloc[sorted_idx]
y_pred_sorted = y_pred[sorted_idx]

# Plot
plt.scatter(X_test, y_test, label="Actual", color="blue")
plt.plot(X_test_sorted, y_pred_sorted, label="Predicted", color="red")
plt.title("Linear Regression Model")
plt.xlabel("In Quantities")
plt.ylabel("Out Quantities")
plt.legend()
plt.show()

# Evaluation
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

print("MSE:", mse)
print("RMSE:", rmse)
print("R2 Score:", r2)
