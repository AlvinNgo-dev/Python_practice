import pandas as pd

df1 = pd.DataFrame({
    "CustomerID": [1, 2, 3, 4, 5],
    "Name": ["Alice", "Bob", "Charlie", "Diana", "Evan"],
    "Gender": ["Female", "Male", "Male", "Female", "Male"],
    "Country": ["USA", "Canada", "USA", "UK", "USA"],
    "Age": [25, 30, None, 28, 35],
    "LoyaltyScore": [None, 80, 75, None, None]
})

print("Original dataset:\n", df1)


# Drop any collumns with more than 50% missing values
threshold = len(df1) * 0.5
df1 = df1.dropna(axis=1, thresh=threshold)
print("Modified dataset:\n", df1)

# Merge three datasets and analyze relationships between them
df2 = pd.DataFrame({
    "OrderID": [101, 102, 103, 104, 105],
    "CustomerID": [1, 2, 3, 1, 4],
    "ProductID": [201, 202, 203, 202, 201],
    "OrderStatus": ["Shipped", "Cancelled", "Shipped", "Pending", "Shipped"],
    "PaymentMethod": ["Credit Card", "PayPal", "Credit Card", "Debit Card", "PayPal"],
    "Discount": [None, 10, None, None, None]
})

df3 = pd.DataFrame({
    "ProductID": [201, 202, 203, 204],
    "ProductName": ["Laptop", "Headphones", "Chair", "Desk"],
    "Category": ["Electronics", "Electronics", "Furniture", "Furniture"],
    "Price": [1200, 150, 300, 450],
    "Brand": ["Dell", "Sony", "Ikea", "Ikea"]
})

# Keeps only matching rows in both tables.
merged1 = pd.merge(df1, df2, on="CustomerID")
merged2 = pd.merge(merged1, df3, on="ProductID")
print("Merged dataset:\n", merged2)

# Convert categorical data to numerical using one-hot encoding
encoded = pd.get_dummies(
    merged2,
    columns=["Gender", "Country", "OrderStatus",
             "PaymentMethod", "Category", "Price", "Brand"]
)
print("One-hot enccoding dataset:\n", encoded)

merged2 = merged2.to_csv(
    "Theory and Practices\Data Cleaning and Preparation with Pandas\merged_dataset.csv")
