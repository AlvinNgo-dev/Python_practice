import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.datasets import load_diabetes
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.feature_selection import mutual_info_regression
# Load the dataset
data = load_diabetes()
df = pd.DataFrame(data.data, columns=data.feature_names)
df['target'] = data.target

# Display dataset information
print(df.head())
print(df.info())

# Calculate correlation matrix
correlation_matrix = df.corr()

# Plot heat map
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm")
plt.title("Correlation Matrix")
plt.show()

# Select features with high correlation to the target
correlated_features = correlation_matrix['target'].sort_values(ascending=False)
print("Features most correlated with Target:")
print(correlated_features)

# Seperate the features and target
X = df.drop(columns=['target'])
y = df['target']

# Calculate mutual information
mutual_info = mutual_info_regression(X, y)

# Create Dataframe for better visualization
mi_df = pd.DataFrame({'Feature': X.columns, "Mutual Information": mutual_info})
mi_df = mi_df.sort_values(by="Mutual Information", ascending=False)

print("Mutal Information Scores:")
print(mi_df)


# Train a random Forest Model
model = RandomForestRegressor(random_state=42)
model.fit(X, y)
# Get feature importance
feature_importance = model.feature_importances_
# Create Dataframe for better visualization
importance_df = pd.DataFrame(
    {'Feature': X.columns, "Importance": feature_importance})
importance_df = importance_df.sort_values(by="Importance", ascending=False)

print("Feature Importance from Random Forest:")
print(importance_df)

# Plot feature importance
plt.figure(figsize=(10, 6))
plt.barh(importance_df['Feature'], importance_df['Importance'])
plt.gca().invert_yaxis()  # Invert y-axis to have the most important feature on top
plt.xlabel('Importance')
plt.title('Feature Importance from Random Forest')
plt.show()
