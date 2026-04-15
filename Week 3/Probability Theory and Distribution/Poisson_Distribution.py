from scipy.stats import poisson
import numpy as np
import matplotlib.pyplot as plt

lam = 3
x = np.arange(0, 10)
y = poisson.pmf(x, lam)
plt.bar(x, y, color="orange")
plt.title("Poisson Distribution")
plt.show()
