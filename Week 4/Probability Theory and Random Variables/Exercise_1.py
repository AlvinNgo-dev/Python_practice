import numpy as np

# Simulating 10,000 coin flips
rolls = np.random.choice(['heads', 'tails'], size=10000)

# Probability of heads
P_1 = np.sum(rolls == 'heads') / len(rolls)
P_2 = np.sum(rolls == 'tails') / len(rolls)
print(f'Probabily of heads: {P_1}')
print(f'Probabily of tails: {P_2}')
