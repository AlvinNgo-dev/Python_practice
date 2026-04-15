import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt

np.random.seed(0)

# Simulated dataset
data = pd.DataFrame({
    "value": np.concatenate([
        np.random.normal(50, 5, 300),
        np.random.normal(60, 6, 300),
        np.random.normal(70, 7, 300)
    ]),
    "group": ["A"]*300 + ["B"]*300 + ["C"]*300
})

sample_size = 50

stratified_sample = data.groupby("group").apply(
    lambda x: x.sample(sample_size)
)

results = []

for group, df in stratified_sample.groupby("group"):

    mean = df["value"].mean()
    std = df["value"].std()
    n = len(df)

    ci_low, ci_high = stats.t.interval(
        0.95,
        df=n-1,
        loc=mean,
        scale=std/np.sqrt(n)
    )

    results.append([group, mean, ci_low, ci_high])

ci_df = pd.DataFrame(results, columns=[
    "Group", "Mean", "CI Lower", "CI Upper"
])

print(ci_df)


means = ci_df["Mean"]
lower = ci_df["CI Lower"]
upper = ci_df["CI Upper"]

errors = [means - lower, upper - means]

plt.figure(figsize=(8, 5))

plt.errorbar(
    ci_df["Group"],
    means,
    yerr=errors,
    fmt='o',
    capsize=5
)

plt.title("Confidence Intervals Across Strata")
plt.ylabel("Mean Value")
plt.xlabel("Stratum")

plt.grid(True)
plt.show()

iterations = 30
records = []

for i in range(iterations):

    sample = data.groupby("group").apply(
        lambda x: x.sample(40)
    )

    for g, df in sample.groupby("group"):

        mean = df["value"].mean()
        std = df["value"].std()
        n = len(df)

        ci = stats.t.interval(
            0.95,
            df=n-1,
            loc=mean,
            scale=std/np.sqrt(n)
        )

        records.append([i, g, mean, ci[0], ci[1]])

multi_ci = pd.DataFrame(records,
                        columns=["sample", "group", "mean", "low", "high"])

plt.figure(figsize=(10, 6))

for g in multi_ci["group"].unique():

    subset = multi_ci[multi_ci["group"] == g]

    plt.errorbar(
        subset["sample"],
        subset["mean"],
        yerr=[subset["mean"]-subset["low"],
              subset["high"]-subset["mean"]],
        fmt='o',
        label=f"Group {g}"
    )

plt.legend()
plt.title("Confidence Intervals from Multiple Stratified Samples")
plt.xlabel("Sample Iteration")
plt.ylabel("Mean")
plt.show()
