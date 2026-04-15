import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

# Synthetic dataset
X = np.random.randn(500, 1)
true_w = np.array([[3.0]])   # Make it 2D for consistency
y = X @ true_w + np.random.randn(500, 1) * 0.5


def mse_loss(X, y, w):
    return np.mean((y - X @ w) ** 2)


def sgd(X, y, batch_size, lr=0.01, epochs=20):
    n_samples, n_features = X.shape
    w = np.random.randn(n_features, 1)  # Consistent shape
    losses = []

    for _ in range(epochs):
        indices = np.random.permutation(n_samples)
        X_shuffled = X[indices]
        y_shuffled = y[indices]

        for i in range(0, n_samples, batch_size):
            X_batch = X_shuffled[i:i + batch_size]
            y_batch = y_shuffled[i:i + batch_size]

            # Gradient of MSE
            gradient = -2 * X_batch.T @ (y_batch - X_batch @ w) / len(X_batch)
            w -= lr * gradient

        losses.append(mse_loss(X, y, w))

    return w, losses


# Train both methods
w_sgd, losses_sgd = sgd(X, y, batch_size=1)
w_mini, losses_mini = sgd(X, y, batch_size=16)

# Plot comparison
plt.figure()
plt.plot(losses_sgd, label="Vanilla SGD (batch=1)")
plt.plot(losses_mini, label="Mini-Batch SGD (batch=16)")
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.title("SGD vs Mini-Batch SGD")
plt.legend()
plt.show()

print("Final weight (Vanilla SGD):", w_sgd.flatten())
print("Final weight (Mini-Batch SGD):", w_mini.flatten())
