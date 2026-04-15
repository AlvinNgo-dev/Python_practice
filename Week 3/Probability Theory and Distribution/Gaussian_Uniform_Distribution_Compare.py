import numpy as np
import matplotlib.pyplot as plt

# Set seed
np.random.seed(42)

# Generate continuous data
sample_size = 10000
gaussian_data = np.random.normal(loc=0, scale=1, size=sample_size)
uniform_data = np.random.uniform(low=-3, high=3, size=sample_size)

# Plot histogram comparison
plt.figure()
plt.hist(gaussian_data, bins=50, density=True, alpha=0.6)
plt.hist(uniform_data, bins=50, density=True, alpha=0.6)

plt.title("Gaussian vs Uniform Distribution")
plt.xlabel("Value")
plt.ylabel("Density")
plt.legend(["Gaussian (Normal)", "Uniform"])
plt.show()
