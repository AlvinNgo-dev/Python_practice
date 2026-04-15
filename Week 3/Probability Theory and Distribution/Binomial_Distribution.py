from scipy.stats import binom
import numpy as np
import matplotlib.pyplot as plt

n, p = 10, 0.5
x = np.arange(0, n+1)
y = binom.pmf(x, n, p)
plt.bar(x, y, color="green")
plt.title("Binomial Distribution")
plt.show()
