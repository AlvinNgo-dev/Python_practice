import pandas as pd

data = {
    "student_id": [1, 2, 3, 4, 5, 6],
    "class": ["A", "A", "A", "B", "B", "B"],
    "score": [70, 80, 90, 60, 65, 75]
}

df = pd.DataFrame(data)
print(df)


def range_func(x):
    return x.max() - x.min()
# Custom aggregation function that computes range


stats = df.groupby("class")["score"].agg(range_func)
# Applies the custom range function per category
print(stats)


def variance_func(x):
    mean = x.mean()
    return ((x - mean) ** 2).mean()


stats = df.groupby("class")["score"].agg(variance_func)
# Applies the variance function per category
print(stats)
