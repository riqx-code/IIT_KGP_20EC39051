import numpy as np
import matplotlib.pyplot as plt

# Number of random pairs to generate
num_samples = 1000

# Generate pairs of independent uniform random variables (U1, U2)
u1 = np.random.rand(num_samples)
u2 = np.random.rand(num_samples)

# Apply the Box-Muller transform to generate standard Gaussian random variables (X, Y)
r = np.sqrt(-2 * np.log(u1))
theta = 2 * np.pi * u2
x = r * np.cos(theta)
y = r * np.sin(theta)

# Plot histograms for X and Y
plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
plt.hist(x, bins=20, density=True, alpha=0.6, color='blue', label='X')
plt.title('Histogram of X (Standard Gaussian)')
plt.xlabel('Value')
plt.ylabel('Probability')
plt.legend()

plt.subplot(1, 3, 2)
plt.hist(y, bins=20, density=True, alpha=0.6, color='green', label='Y')
plt.title('Histogram of Y (Standard Gaussian)')
plt.xlabel('Value')
plt.ylabel('Probability')
plt.legend()

# Plot a scatter plot of the generated pairs
plt.subplot(1, 3, 3)
plt.scatter(x, y, alpha=0.5, s=20, color='blue')
plt.title('Scatter Plot of Standard Gaussian Pairs (X, Y)')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)
plt.axis('equal')

plt.tight_layout()
plt.show()
