import pandas as pd
# Series
s = pd.Series([10, 20, 30], index=["a", "b", "c"])
print(s)

# DataFrame
data = {"Name": ["Alice", "Bob"], "Age": [25, 30]}
df = pd.DataFrame(data)
print(df)
