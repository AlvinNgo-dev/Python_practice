import pandas as pd

df = pd.read_excel("E:\OEE.xlsx")
print(f"Original data frame:\n{df}")

df2 = pd.DataFrame(df)
print(f"New data frame:\n{df2}")

df2.to_excel("Data_frame.xlsx")

file = pd.read_csv("E:\OEE_data_log.csv")
print(file)
