import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# -------------------------------------------------
# Step 1: Define symbolic variable and function
# -------------------------------------------------
x = sp.Symbol('x')

# Quadratic function
f = x**2 + 4*x + 4

# Compute symbolic derivative
df = sp.diff(f, x)

print("Function:", f)
print("Derivative:", df)

# Convert symbolic expressions to numerical functions
f_numeric = sp.lambdify(x, f, 'numpy')
df_numeric = sp.lambdify(x, df, 'numpy')

# -------------------------------------------------
# Step 2: Gradient Descent Implementation
# -------------------------------------------------


def gradient_descent(starting_point, learning_rate, iterations):
    x_current = starting_point
    history = [x_current]

    for i in range(iterations):
        gradient = df_numeric(x_current)
        x_current = x_current - learning_rate * gradient
        history.append(x_current)

    return history


# Parameters
initial_x = 5
learning_rate = 0.1
iterations = 15

# Run gradient descent
x_history = gradient_descent(initial_x, learning_rate, iterations)

# -------------------------------------------------
# Step 3: Visualization
# -------------------------------------------------
x_vals = np.linspace(-6, 4, 400)
y_vals = f_numeric(x_vals)

plt.figure(figsize=(10, 6))
plt.plot(x_vals, y_vals, label="f(x) = x² + 4x + 4")

# Plot descent points
for x_point in x_history:
    plt.scatter(x_point, f_numeric(x_point), color='red')

# Connect descent path
plt.plot(x_history, f_numeric(np.array(x_history)), color='red',
         linestyle='--', label="Gradient Descent Path")

plt.title("Gradient Descent on a Quadratic Function")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.grid(True)

plt.show()
