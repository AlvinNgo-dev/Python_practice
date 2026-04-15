# ============================================
# 1. Loss Surface + SGD Path (No 3D Toolkit)
# ============================================

import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

# Generate synthetic linear regression data
X = np.linspace(-1, 1, 100)
true_w1 = 2.0
true_w0 = -1.0
y = true_w1 * X + true_w0 + np.random.normal(0, 0.2, size=X.shape)

# Mean Squared Error


def compute_loss(w0, w1):
    y_pred = w1 * X + w0
    return np.mean((y - y_pred) ** 2)

# Analytical gradients


def compute_gradients(w0, w1):
    y_pred = w1 * X + w0
    dw0 = -2 * np.mean(y - y_pred)
    dw1 = -2 * np.mean((y - y_pred) * X)
    return dw0, dw1


# ===============================
# SGD Optimization
# ===============================
learning_rate = 0.1
epochs = 30

w0, w1 = -2.0, 2.0   # initial guess
path = [(w0, w1)]
losses = [compute_loss(w0, w1)]

for _ in range(epochs):
    dw0, dw1 = compute_gradients(w0, w1)
    w0 -= learning_rate * dw0
    w1 -= learning_rate * dw1
    path.append((w0, w1))
    losses.append(compute_loss(w0, w1))

path = np.array(path)

# ===============================
# Compute Loss Surface Grid
# ===============================
w0_vals = np.linspace(-3, 3, 200)
w1_vals = np.linspace(-3, 3, 200)

W0, W1 = np.meshgrid(w0_vals, w1_vals)
Loss = np.zeros_like(W0)

for i in range(W0.shape[0]):
    for j in range(W0.shape[1]):
        Loss[i, j] = compute_loss(W0[i, j], W1[i, j])

# ===============================
# Plot Contour + SGD Path
# ===============================
plt.figure(figsize=(8, 6))
contours = plt.contour(W0, W1, Loss, levels=30)
plt.clabel(contours, inline=True, fontsize=8)

# Plot optimization trajectory
plt.plot(path[:, 0], path[:, 1], 'ro-', label='SGD Path')

plt.xlabel("w0 (bias)")
plt.ylabel("w1 (weight)")
plt.title("Loss Surface (Contour) and SGD Optimization Path")
plt.legend()
plt.grid(True)
plt.show()

# ===============================
# Plot Loss vs Iteration
# ===============================
plt.figure(figsize=(6, 4))
plt.plot(losses)
plt.xlabel("Iteration")
plt.ylabel("Loss")
plt.title("Loss Decrease During SGD")
plt.grid(True)
plt.show()
