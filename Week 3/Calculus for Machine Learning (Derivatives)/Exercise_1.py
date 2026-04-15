import sympy as sp

# Define a function
x = sp.Symbol('x')
f = x ** 3 - 5*x + 7

# Compute Derivative
derivative = sp.diff(f, x)

print("Function: ", f)
print("Derivative: ", derivative)

# Define a multivariable function
x, y = sp.symbols('x y')
f = x ** 2 + 3*y ** 2 - 4*x*y

# Compute partial derivatives
grad_x = sp.diff(f, x)
grad_y = sp.diff(f, y)

print("Function:", f)
print("Grad X:", grad_x)
print("Grad Y:", grad_y)
