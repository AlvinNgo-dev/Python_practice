import pandas as pd
import plotly.express as px
from plotly.subplots import make_subplots

# Load data
df = pd.read_csv(
    "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
)

# Cleaning
df["Age"] = df["Age"].fillna(df["Age"].median())
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])
df = df.drop_duplicates()

# Aggregation
survival_by_class = df.groupby("Pclass")["Survived"].mean().reset_index()

# Create subplots
fig = make_subplots(
    rows=2, cols=2,
    subplot_titles=[
        "Survival Rate by Class",
        "Age Distribution",
        "Age vs Fare",
        "Fare Distribution"
    ]
)

# Bar chart
bar = px.bar(survival_by_class, x="Pclass", y="Survived")
fig.add_trace(bar.data[0], row=1, col=1)

# Histogram
hist_age = px.histogram(df, x="Age", nbins=20)
fig.add_trace(hist_age.data[0], row=1, col=2)

# Scatter
scatter = px.scatter(df, x="Age", y="Fare", opacity=0.5)
fig.add_trace(scatter.data[0], row=2, col=1)

# Histogram Fare
hist_fare = px.histogram(df, x="Fare", nbins=20)
fig.add_trace(hist_fare.data[0], row=2, col=2)

fig.update_layout(
    height=800,
    width=1000,
    title_text="Titanic Data Dashboard",
    showlegend=False
)

fig.show()
