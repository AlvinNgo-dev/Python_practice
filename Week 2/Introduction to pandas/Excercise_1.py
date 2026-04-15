# https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv

import pandas as pd

# Load Dataset
df = pd.read_csv(
    "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")

# Explore structure
print("First 5 rows: \n", df.head())
print("Last 5 rows: \n", df.tail(5))
print(df.info())
print(df.describe())
print(df.iloc[0])  # print 1st row
print(df.iloc[:, 0])  # print 1st collumn
print(df.loc[:, "species"])  # print by label
print(df[["species", "sepal_length"]])
print(df[(df["sepal_length"] > 5) & (df["species"] == "setosa")])
