import numpy as np  # Import NumPy library for numerical and matrix operations

# Define the gradient descent function


def gradient_descent(X, y, theta, learning_rate, iterations):
    """
    Performs gradient descent to find the optimal theta parameters.

    Parameters:
    X : Feature matrix (m x n) where m = number of samples, n = number of features
        Includes a column of 1s for the bias (intercept) term.
    y : Actual target values (m x 1)
    theta : Initial parameter values (n x 1)
    learning_rate : Step size for updating theta
    iterations : Number of times to update theta

    Returns:
    theta : Optimized parameter values after gradient descent
    """

    m = len(y)  # Number of training examples

    # Loop for a fixed number of iterations to gradually improve theta
    for _ in range(iterations):

        # Step 1: Compute predicted values using current theta
        # Formula: predictions = X * theta
        predictions = np.dot(X, theta)

        # Step 2: Compute error (difference between predicted and actual values)
        # Formula: error = predictions - actual values
        errors = predictions - y

        # Step 3: Compute gradients (partial derivatives of cost function)
        # Formula: gradient = (1/m) * X^T * errors
        # This tells us the direction and magnitude to adjust theta
        gradients = (1/m) * np.dot(X.T, errors)

        # Step 4: Update theta values
        # Move theta in the opposite direction of gradient to reduce error
        # Formula: theta = theta - learning_rate * gradient
        theta -= learning_rate * gradients

    # Return the optimized parameters after all iterations
    return theta


# -------------------------
# Sample Data
# -------------------------

# Feature matrix
# First column = 1 (bias term)
# Second column = actual feature values
X = np.array([
    [1, 1],
    [1, 2],
    [1, 3]
])

# Target values (actual outputs)
y = np.array([2, 2.5, 3.5])

# Initial guess for parameters
# theta[0] = intercept (bias)
# theta[1] = slope (weight)
theta = np.array([0.1, 0.1])

# Learning rate controls how fast the model learns
learning_rate = 0.1

# Number of iterations for gradient descent
iterations = 1000

# Perform gradient descent to find best theta values
optimized_theta = gradient_descent(X, y, theta, learning_rate, iterations)

# Print final optimized parameters
print("Optimized Parameters:", optimized_theta)
