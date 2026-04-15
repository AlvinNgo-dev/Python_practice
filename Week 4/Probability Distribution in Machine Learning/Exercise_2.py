# Simulate random variables from custom distributions

# Inverse Transform Sampling
import numpy as np
import matplotlib.pyplot as plt

# generate uniform numbers
u = np.random.uniform(0, 1, 10000)

# inverse transform
x = np.sqrt(u)

plt.hist(x, bins=50, density=True)
plt.title("Samples from custom distribution F(x)=x^2")
plt.show()

# Rejection Sampling


def target_pdf(x):
    return 2*x


samples = []

while len(samples) < 10000:

    x = np.random.uniform(0, 1)
    y = np.random.uniform(0, 2)  # maximum of pdf

    if y < target_pdf(x):
        samples.append(x)

samples = np.array(samples)

plt.hist(samples, bins=50, density=True)
plt.title("Rejection Sampling")
plt.show()

# Sampling from Arbitrary PDF


x = np.linspace(-4, 4, 1000)

pdf = np.exp(-x**2/2)*(1+0.5*np.sin(5*x))
pdf[pdf < 0] = 0

cdf = np.cumsum(pdf)
cdf = cdf/cdf[-1]

# Generate uniform samples
u = np.random.rand(10000)

samples = np.interp(u, cdf, x)

plt.hist(samples, bins=60, density=True)
plt.title("Custom Arbitrary Distribution")
plt.show()

# Creating a Custom Random Generator Function


def custom_random(n):

    u = np.random.randint(0, 500, size=n)

    # inverse CDF example
    x = np.sqrt(u)

    return x


data = custom_random(10000)
print(data)
