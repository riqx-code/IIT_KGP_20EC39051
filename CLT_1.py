import random
import matplotlib.pyplot as plt
import numpy as np

# Function to generate and normalize random variables
def generate_normalized_variables(n, num_experiments):
    normalized_variables = []
    for _ in range(num_experiments):
        random_variables = [random.uniform(0, 10) for _ in range(n)]
        mean = sum(random_variables) / n
        variance = sum((x - mean) ** 2 for x in random_variables) / (n - 1)
        normalized = [(x - mean) / np.sqrt(variance) for x in random_variables]
        y_j = (1 / np.sqrt(n)) * sum(normalized)
        normalized_variables.append(y_j)
    return normalized_variables

# Parameters
n = 1000
num_experiments = 10000

# Generate normalized variables and compute Y_j
normalized_variables = generate_normalized_variables(n, num_experiments)

# Plotting histogram
plt.figure()
plt.hist(normalized_variables, bins=50, density=True, color='blue', alpha=0.7)
plt.xlabel('Value of Y_j')
plt.ylabel('Approximate Density')
plt.title('Histogram of Y_j (Normalized Random Variables)')
plt.grid(True)
plt.show()
