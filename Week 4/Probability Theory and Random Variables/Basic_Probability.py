from itertools import product

# Sample space of a dice roll
sample_space = list(range(1, 7))

# Probability of rolling an even number
even_numbers = [2, 4, 6]
P_even = len(even_numbers) / len(sample_space)
print("P(Even):", P_even)
