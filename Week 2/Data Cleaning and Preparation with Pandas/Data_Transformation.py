import pandas as pd

df = pd.DataFrame({
    "fname": ["Alice", "Bob"],
    "age": [20, 25]
})
# Renames one (or more) columns in a DataFrame.
df = df.rename(columns={"fname": "first_name"})
print(df)

df = pd.DataFrame({
    "score": [10, 20, 30]
})
# Converts a column to a specific data type.
df["score"] = df["score"].astype("float")
print(df.dtypes)

df = pd.DataFrame({
    "date": ["2024-01-01", "2024-02-15"]
})
# Converts a column into datetime objects
df["date"] = pd.to_datetime(df["date"])
print(df.dtypes)
df["date"].dt.year
df["date"].dt.month
df["date"].dt.day

df = pd.DataFrame({
    "salary": [3000, 4000, 5000]
})
# Creates a new derived column from an existing one.
df["double_salary"] = df["salary"] * 2
print(df)
