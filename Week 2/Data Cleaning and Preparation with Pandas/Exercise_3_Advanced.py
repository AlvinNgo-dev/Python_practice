import pandas as pd

# =========================
# INPUT DATA (RAW DATASETS)
# =========================

df1 = pd.DataFrame({
    "CustomerID": [1, 2, 3, 4, 5],
    "Name": ["Alice", "Bob", "Charlie", "Diana", "Evan"],
    "Gender": ["Female", "Male", "Male", "Female", "Male"],
    "Country": ["USA", "Canada", "USA", "UK", "USA"],
    "Age": [25, 30, None, 28, 35],
    "LoyaltyScore": [None, 80, 75, None, None]
})

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

# =========================
# PROCESSING FUNCTIONS
# =========================


def drop_missing_columns(df, ratio=0.5):
    threshold = len(df) * ratio
    return df.dropna(axis=1, thresh=threshold)


def merge_datasets(customers, orders, products):
    merged = pd.merge(customers, orders, on="CustomerID")
    merged = pd.merge(merged, products, on="ProductID")
    return merged


def one_hot_encode(df):
    return pd.get_dummies(
        df,
        columns=[
            "Gender", "Country",
            "OrderStatus", "PaymentMethod",
            "Category", "Brand"
        ]
    )

# =========================
# PIPELINE (EXECUTION)
# =========================


print("Original dataset:\n", df1)

df1_clean = drop_missing_columns(df1)
print("\nModified dataset:\n", df1_clean)

merged = merge_datasets(df1_clean, df2, df3)
print("\nMerged dataset:\n", merged)

encoded = one_hot_encode(merged)
print("\nOne-hot encoding dataset:\n", encoded)
