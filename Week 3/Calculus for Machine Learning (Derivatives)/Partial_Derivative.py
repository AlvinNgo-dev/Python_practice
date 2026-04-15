import sympy as sp

x, y = sp.symbols('x y')
f = x**2 + y**2
gradient_x = sp.diff(f, x)
gradient_y = sp.diff(f, y)

print(f"Partial Derivatives: {gradient_x}, {gradient_y}")
