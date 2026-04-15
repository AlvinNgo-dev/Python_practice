import sympy as sp

x = sp.Symbol('x')
f = x**2
derivatives = sp.diff(f, x)

print(f"Derivative of {f} is: {derivatives}")
