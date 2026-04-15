import pandas as pd

df1 = pd.DataFrame({
    "id": [1, 2],
    "name": ["Alice", "Bob"]
})

df2 = pd.DataFrame({
    "id": [3, 4],
    "name": ["Carol", "Dan"]
})
# Stacks DataFrames vertically (row-wise).
combined = pd.concat([df1, df2], axis=0)
print(combined)

df1 = pd.DataFrame({
    "name": ["Alice", "Bob"]
})

df2 = pd.DataFrame({
    "age": [20, 25]
})
# Stacks DataFrames horizontally (column-wise).
combined = pd.concat([df1, df2], axis=1)
print(combined)

df1 = pd.DataFrame({
    "id": [1, 2, 3],
    "name": ["A", "B", "C"]
})

df2 = pd.DataFrame({
    "id": [2, 3, 4],
    "score": [80, 90, 70]
})
# Keeps only matching rows in both tables.
merged = pd.merge(df1, df2, on="id")
print(merged)
# Keeps all rows from df1, matches from df2.
merged = pd.merge(df1, df2, how="left", on="id")
print(merged)

df1 = pd.DataFrame({
    "name": ["Alice", "Bob"]
}, index=[1, 2])

df2 = pd.DataFrame({
    "score": [90, 80]
}, index=[1, 3])
# Joins DataFrames using their index, not a column.
joined = df1.join(df2, how="inner")
print(joined)
