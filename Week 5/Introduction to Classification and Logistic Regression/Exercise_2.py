# Same as Excercise_1.py by with real-world dataset
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report
from sklearn.preprocessing import StandardScaler

# 1. Load the real-world dataset directly from a public URL
url = "https://raw.githubusercontent.com/shivang98/Social-Network-ads-Boost/master/Social_Network_Ads.csv"
df = pd.read_csv(url)

# 2. Select Features (Age, Salary) and Target (Purchased)
X = df[['Age', 'EstimatedSalary']]
y = df['Purchased']

# 3. Split Data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 4. Scale the features (Crucial step for real-world data with varying magnitudes)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 5. Train the logistic regression model
model = LogisticRegression()
model.fit(X_train_scaled, y_train)

# 6. Make Predictions
y_pred = model.predict(X_test_scaled)

# 7. Evaluate performance
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Precision:", precision_score(y_test, y_pred))
print("Recall:", recall_score(y_test, y_pred))
print("F1 Score:", f1_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# 1. Define boundaries using scaled test data
X1 = X_test_scaled[:, 0]
X2 = X_test_scaled[:, 1]
x_min, x_max = X1.min() - 1, X1.max() + 1
y_min, y_max = X2.min() - 1, X2.max() + 1

xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.01),
                     np.arange(y_min, y_max, 0.01))

# 2. Predict grid points
Z = model.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

# 3. Create the Plot
plt.figure(figsize=(10, 6))

# Plot boundary
contour = plt.contourf(xx, yy, Z, alpha=0.3, cmap="coolwarm")

# Plot data points and capture the scatter object for the legend
scatter = plt.scatter(X1, X2, c=y_test, edgecolor="k", cmap="coolwarm", s=50)

# 4. Add Legend for the variables
# This automatically extracts the colors and labels (0 and 1) from the scatter plot
legend1 = plt.legend(*scatter.legend_elements(),
                     title="Outcome", loc="upper left")
plt.gca().add_artist(legend1)

# Manually define labels for clarity
# 0 = Not Purchased (Blue), 1 = Purchased (Red)
labels = ["Not Purchased", "Purchased"]
for i, label in enumerate(labels):
    legend1.get_texts()[i].set_text(label)

# 5. Add Plot Details
plt.title("Logistic Regression: Age vs Salary Impact on Purchase")
plt.xlabel("Age (Standardized)")
plt.ylabel("Estimated Salary (Standardized)")
plt.grid(True, linestyle='--', alpha=0.5)

plt.show()
