import numpy as np
import random
import scipy.stats as stats
import math
data = np.random.choice(np.arange(10, 50, 10), size=5)
print(data)
mean = sum(data) / len(data)

variance = sum((x - mean) ** 2 for x in data) / len(data)
std_dev = variance ** 0.5

sample_mean = mean
z_score = stats.t.ppf(0.975, df=len(data)-1)

ci = (sample_mean - z_score * (std_dev / len(data) ** 0.5),
      sample_mean + z_score * (std_dev / len(data) ** 0.5))

ci_rounded_up = (
    math.ceil(ci[0] * 100) / 100,
    math.ceil(ci[1] * 100) / 100
)

print("95% CI (rounded up to 2 decimals):", ci_rounded_up)
