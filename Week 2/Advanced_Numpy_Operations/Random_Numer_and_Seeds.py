import numpy as np

# np.random.seed(31)    #Keeps program generating the same value for a specific seed

random_array = np.random. rand(3, 3)
print("Random Array: \n", random_array)

random_integers = np.random.randint(0, 10, size=(2, 3))
print("Random Integers: \n", random_integers)
