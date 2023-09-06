import random
import matplotlib.pyplot as plt
import numpy as np

# Function to generate uniform random variables and compute their mean
def generate_uniform_means(n_values):
    means = []
    for n in n_values:
        random_variables = [random.uniform(0, 10) for _ in range(n)]
        mean = sum(random_variables) / n
        means.append(mean)
    return means

# Sample sizes
n_values = [10, 100, 1000, 10000, 100000, 1000000, 10000000]

# Generate means
means = generate_uniform_means(n_values)

# Plotting
plt.figure()
plt.plot(n_values, means, marker='o')
plt.xscale('log')  # Set x-axis to logarithmic scale
plt.xlabel('Sample Size (n)')
plt.ylabel('Arithmetic Mean')
plt.title('Arithmetic Mean vs. Sample Size (Uniform Random Variables)')
plt.grid(True)
plt.show()
