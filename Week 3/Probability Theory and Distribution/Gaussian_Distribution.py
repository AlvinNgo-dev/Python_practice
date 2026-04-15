import numpy as np
import matplotlib.pyplot as plt

# Define the mean (mu) and standard deviation (sigma) of the Gaussian distribution
mu, sigma = 0, 1

# Create 100 evenly spaced values between -4 and 4
# These will be the x-axis values
x = np.linspace(-4, 4, 100)

# Compute the Gaussian (Normal) distribution formula:
# f(x) = (1 / sqrt(2*pi*sigma^2)) * e^(-0.5 * ((x - mu)/sigma)^2)
# This calculates the probability density for each x value
y = (1 / (np.sqrt(2*np.pi * sigma ** 2))) * np.exp(-0.5*((x-mu) / sigma) ** 2)

# Plot x values against their corresponding Gaussian probabilities
plt.plot(x, y)
plt.title("Gaussian Distribution")
plt.show()
