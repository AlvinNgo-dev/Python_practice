# Fit a multiple linear regression model with multiple independent variables

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    'Size': [1500, 1800, 1200, 2000, 1700],
    'Bedrooms': [3, 4, 2, 4, 3],
    'Age': [10, 5, 20, 8, 12],
    'Price': [300000, 360000, 200000, 400000, 340000]
}

df = pd.DataFrame(data)

X = df[['Size', 'Bedrooms', 'Age']]
y = df['Price']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)
# model.fit(X_test, y_test)
print("Intercept:", model.intercept_)
print("Coefficients:", model.coef_)

corr = df.corr()
sns.heatmap(corr, annot=True)
plt.show()
