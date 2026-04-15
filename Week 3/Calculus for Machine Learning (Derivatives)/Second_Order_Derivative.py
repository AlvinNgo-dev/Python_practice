import sympy as sp

x = sp.symbols('x')
f = x**3 + x**2 + 1
second_derivative = sp.diff(f, x, 2)
print("Second derivative:", second_derivative)

# Define variables
x, y = sp.symbols('x y')

# Define function
f = x**3 + x*y + y**2

# Compute Hessian matrix
H = sp.hessian(f, (x, y))

print(H)
