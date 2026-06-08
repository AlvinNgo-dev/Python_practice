import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV

# Load the Titanic dataset
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

# Select features and target variable
df = df[["Pclass", "Sex", "Age", "Fare", "Embarked", "Survived"]]

# Handle missing values (basic filling; pipelines also include imputers)
# Avoid chained-assignment / copy-on-write warnings by assigning the result back to the columns
df["Age"] = df["Age"].fillna(df["Age"].median())
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

# Define features and target variable
X = df.drop(columns=["Survived"])
y = df["Survived"]

# Apply feature scaling and encoding
numeric_pipeline = Pipeline(steps=[
    ("imputer", SimpleImputer(strategy="median")),
    ("scaler", StandardScaler())
])
categorical_pipeline = Pipeline(steps=[
    ("imputer", SimpleImputer(strategy="most_frequent")),
    ("onehot", OneHotEncoder(handle_unknown="ignore"))
])
preprocessor = ColumnTransformer(
    transformers=[
        ("num", numeric_pipeline, ["Age", "Fare"]),
        ("cat", categorical_pipeline, ["Pclass", "Sex", "Embarked"])
    ]
)

# Preprocess features
X_preprocessed = preprocessor.fit_transform(X)

# Evaluate Logistic Regression model using cross-validation
log_model = LogisticRegression(solver="liblinear", max_iter=200)
log_scores = cross_val_score(
    log_model, X_preprocessed, y, cv=5, scoring='accuracy')
print(
    f"Logistic Regression Cross-Validation Accuracy: {log_scores.mean():.2f}")

# Train and evaluate Random Forest model using cross-validation
rf_model = RandomForestClassifier(random_state=42)
rf_scores = cross_val_score(
    rf_model, X_preprocessed, y, cv=5, scoring='accuracy')
print(f"Random Forest Cross-Validation Accuracy: {rf_scores.mean():.2f}")

# Define hyperparameters grid
param_grid = {
    "n_estimators": [50, 100, 200],
    "max_depth": [None, 10, 20],
    "min_samples_split": [2, 5, 10]
}

# Perform Grid Search
grid_search = GridSearchCV(
    estimator=rf_model,
    param_grid=param_grid,
    cv=5,
    scoring='accuracy',
    n_jobs=-1
)
grid_search.fit(X_preprocessed, y)

# Display best hyperparameters and corresponding accuracy
print(f"Best Hyperparameters: {grid_search.best_params_}")
print(f"Best Cross-Validation Accuracy: {grid_search.best_score_:.2f}")
