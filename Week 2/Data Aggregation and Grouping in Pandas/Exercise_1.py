import pandas as pd

data = {
    "order_id": [1, 2, 3, 4, 5, 6],
    "region": ["North", "South", "North", "East", "South", "East"],
    "product_category": ["Electronics", "Electronics", "Furniture", "Furniture", "Electronics", "Furniture"],
    "sales": [1000, 1500, 800, 1200, 2000, 900]
}

df = pd.DataFrame(data)
print("Original dataset:\n", df)

grouped = df.groupby("region")["order_id"].mean()
grouped_2 = df.groupby("product_category")["sales"].mean()
print("Grouped Categorical:\n", grouped, "\n", grouped_2)
