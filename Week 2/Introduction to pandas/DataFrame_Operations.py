import pandas as pd

s = pd.Series([10, 20, 30], index=["a", "b", "c"])
data = {"Name": ["Alice", "Bob"], "Age": [25, 30]}
df = pd.DataFrame(data)

# Save data to file
df.to_csv("Theory and Practices\Introduction to pandas\data.csv", index=False)
# df.to_excel("Theory and Practices\Introduction to pandas\data.xlsx")

# Load data from file
df = pd.read_csv("Theory and Practices\Introduction to pandas\data.csv")
# df = pd.read_excel("Theory and Practices\Introduction to pandas\data.xlsx")
# print(df)

# Viewing data
# print(df.head())  # Print first 5 rows
# print(df.tail(3))  # Print last 3 rows

# print(df.info())  # Print information of the data
# print(df.describe())  # Print statistic information of the data

# print(df[["Name", "Age"]])

# print(df[df["Age"] > 25])

print(df.iloc[0])  # print 1st row
print(df.iloc[:, 0])  # print 1st collumn
print(df.loc[:, "Name"])  # print by label
