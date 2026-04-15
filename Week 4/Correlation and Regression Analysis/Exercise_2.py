import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures


x = np.linspace(-10, 10, 100)
y = x**2

df = pd.DataFrame({'x': x, 'y': y})

X = df[['x']]
model = LinearRegression()
model.fit(X, y)

print(model.score(X, y))


poly = PolynomialFeatures(degree=2)
X_poly = poly.fit_transform(X)

model = LinearRegression()
model.fit(X_poly, y)

print(model.score(X_poly, y))
