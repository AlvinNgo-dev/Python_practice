import pandas as pd

import pandas as pd

data = {
    "order_id": [1, 2, 3, 4, 5, 6, 7, 8],
    "region": ["North", "North", "South", "South", "East", "East", "West", "West"],
    "year":   [2023, 2024, 2023, 2024, 2023, 2024, 2023, 2024],
    "sales":  [1200, 1500, 1000, 1300, 900, 1100, 1400, 1600]
}

df = pd.DataFrame(data)

pivot = df.pivot_table(
    values="sales",
    index="region",
    columns="year",
    aggfunc="mean"
)

# print(pivot)


def range_func(x):
    return x.max() - x.min()
# Custom aggregation function that computes range


stats = df.groupby("year")["sales"].agg(range_func)
# Applies the custom range function per category
print(stats)
