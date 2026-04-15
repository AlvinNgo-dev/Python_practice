import pandas as pd

df = pd.DataFrame({
    "A": [1, 2, None],
    "B": [4, None, 6]
})
# Removes rows that contain any missing value.
df = df.dropna()
print(f"Data Frame 1:\n{df}")

df2 = pd.DataFrame({
    "A": [1, 2, 3],
    "B": [4, None, 6]
})
# Removes columns that contain any missing value.
df2 = df2.dropna(axis=1)
print(f"Data Frame 2:\n{df2}")

df3 = pd.DataFrame({
    "salary": [5000, None, 7000]
})
# Replaces missing values in one column with 0
df3["salary"] = df3["salary"].fillna(0)
print(f"Data Frame 3:\n{df3}")

df4 = pd.DataFrame({
    "temperature": [20, None, None, 25]
})
# Fills missing values using the previous valid value.
df4 = df4.ffill()
print(f"Data Frame 4 Forawrd Fill:\n{df4}")
# Fills missing values using the next valid value.
df4 = df4.bfill()
print(f"Data Frame 4 Backward Fill:\n{df4}")

df5 = pd.DataFrame({
    "sales": [100, None, None, 150]
})
# Fills missing values using mathematical interpolation (estimates values between known points).
df5["sales"] = df5["sales"].interpolate()
print(f"Data Frame 5:\n{df5}")
