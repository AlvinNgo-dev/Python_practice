import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Load Dataset
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"
df = pd.read_csv(url)
# Define variables
X = df['total_bill'] . values. reshape(-1, 1)
y = df['tip'] . values

# Fit linear regression
model = LinearRegression()
model.fit(X, y)

# Output coefficients
print("Slope: ", model.coef_[0])
print("Intercept: ", model.intercept_)
print("R-Squared:", model.score(X, y))

# Plot regression
sns. scatterplot(x=df['total_bill'], y=df['tip'], color="blue")
plt.plot(df['total_bill'], model.predict(X),
         color="red", label="Regression Line")
plt.title("Total Bill vs Tip")
plt. legend()
plt. show()
