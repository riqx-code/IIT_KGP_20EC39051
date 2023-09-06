import numpy as np
import matplotlib.pyplot as plt

# Function to generate and normalize Cauchy random variables
def generate_normalized_cauchy_variables(n, num_experiments):
    normalized_variables = []
    for _ in range(num_experiments):
        cauchy_variables = np.random.standard_cauchy(size=n)
        mean = np.mean(cauchy_variables)
        normalized = (cauchy_variables - mean) / np.sqrt(n)  # Normalization by sqrt(n)
        y_j = np.sum(normalized)
        normalized_variables.append(y_j)
    return normalized_variables

# Parameters
n = 1000
num_experiments = 10000

# Generate normalized Cauchy variables and compute Y_j
normalized_cauchy_variables = generate_normalized_cauchy_variables(n, num_experiments)

# Plotting histogram
plt.figure()
plt.hist(normalized_cauchy_variables, bins=100, density=True, color='blue', alpha=0.7)
plt.xlabel('Value of Y_j')
plt.ylabel('Approximate Density')
plt.title('Histogram of Y_j (Normalized Cauchy Random Variables)')
plt.grid(True)
plt.xlim(-50, 50)  # Adjust x-axis limits for better visualization
plt.show()
