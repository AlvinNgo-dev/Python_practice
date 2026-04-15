import numpy as np
import matplotlib.pyplot as plt

# Set random seed for reproducibility
np.random.seed(42)

# Multinomial distribution parameters
n_trials = 1000
class_probabilities = [0.2, 0.35, 0.25, 0.2]
class_labels = ["Class A", "Class B", "Class C", "Class D"]

# Generate multinomial data
multinomial_sample = np.random.multinomial(n_trials, class_probabilities)

# Plot the results
plt.figure()
plt.bar(class_labels, multinomial_sample)
plt.title("Multinomial Distribution - Multi-Class Data")
plt.xlabel("Class")
plt.ylabel("Number of Observations")
plt.show()
