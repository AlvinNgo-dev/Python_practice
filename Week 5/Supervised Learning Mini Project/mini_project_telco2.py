# Task 1: Perform EDA and Preprocessing
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix

# Load Telco Customer Churn Dataset
df_telco = pd.read_csv(
    'Practice\Theory and Practices\Week 5\Supervised Learning Mini Project\Telco-Customer-Churn.csv')
df_telco.drop(columns=['customerID'], inplace=True)
df_telco = pd.get_dummies(df_telco, drop_first=True)

# Encode categorical variables
le = LabelEncoder()

# Replace Yes/No with 1/0 BEFORE encoding
df_telco['Churn'] = df_telco['Churn'].map({'Yes': 1, 'No': 0})

# Then apply one-hot encoding to other categorical columns
df_telco = pd.get_dummies(df_telco, drop_first=True)

# Define features and target
X = df_telco.drop(columns=['Churn'])
y = df_telco['Churn']

# Scale features
scaler = StandardScaler()
X = scaler.fit_transform(X)

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

# Train logistic regression model
log_model = LogisticRegression(max_iter=200)
log_model.fit(X_train, y_train)

# Train k-NN model
knn_model = KNeighborsClassifier(n_neighbors=5)
knn_model.fit(X_train, y_train)

# Evaluate models
log_pred = log_model.predict(X_test)
knn_pred = knn_model.predict(X_test)

print("\n Logistic Regression Classification Report: ")
print(classification_report(y_test, log_pred))

print("\n k-NN Classification report:")
print(classification_report(y_test, knn_pred))

# Confusion Matrix for Logistic Regression
print("Confusion Matrix: \n", confusion_matrix(y_test, log_pred))
