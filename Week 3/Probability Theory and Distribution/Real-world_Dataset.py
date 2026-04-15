import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Set seed
np.random.seed(42)

# Simulate daily customer arrivals (Poisson distribution)
days = 365
average_customers_per_day = 50
customer_arrivals = np.random.poisson(lam=average_customers_per_day, size=days)

# Basic analysis
mean_arrivals = np.mean(customer_arrivals)
std_arrivals = np.std(customer_arrivals)

print("Mean daily arrivals:", mean_arrivals)
print("Standard deviation:", std_arrivals)

# Plot results
plt.figure()
plt.hist(customer_arrivals, bins=30, density=True)
plt.title("Simulated Daily Customer Arrivals (Poisson Distribution)")
plt.xlabel("Number of Customers")
plt.ylabel("Density")
plt.show()


df = pd.read_csv(
    "Theory and Practices\Week 3\Probability Theory and Distribution\Data.gov_Daily_Visitor_Statistics.csv")
df = pd.DataFrame(df)
df["Date"] = pd.to_datetime(df["Date"])
# replace with actual column name from CSV
df["Total Number of Visitors"] = df["Total Number of Visitors"]

print(df.head())

# Plot results
plt.figure()
plt.plot(df["Date"], df["Total Number of Visitors"])

plt.title("Daily Visitors Over Time")
plt.xlabel("Date")
plt.ylabel("Number of Visitors")

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
