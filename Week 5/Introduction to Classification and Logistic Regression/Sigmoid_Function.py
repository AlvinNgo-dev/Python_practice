import numpy as np
import matplotlib.pyplot as plt

# Sigmoid function


def sigmoid(z):
    return 1/(1 + np.exp(-z))


# Generate value
z = np.linspace(-10, 10, 100)
sigmoit_values = sigmoid(z)

# Plot
plt.plot(z, sigmoit_values)
plt.title("Sigmoid Function")
plt.xlabel("z")
plt.ylabel("sigma(z)")
plt.grid()
plt.show()
