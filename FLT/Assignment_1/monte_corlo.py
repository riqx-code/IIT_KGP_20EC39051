import numpy as np
import matplotlib.pyplot as plt

# Define the target distributions
lamda_poisson = 10
p_binomial = 0.4
n_binomial = 6
lamda_exponential = 2  # Added the exponential distribution

# Function to calculate the Poisson CDF
def poisson_cdf(x, lamda):
    return 1 - np.exp(-lamda * x)

# Function to calculate the Binomial CDF
def binomial_cdf(x, n, p):
    return np.sum([np.math.comb(n, k) * p**k * (1 - p)**(n - k) for k in range(int(x) + 1)])

# Function to calculate the Exponential CDF
def exponential_cdf(x, lamda):
    return 1 - np.exp(-lamda * x)

# Function to generate random samples using Monte Carlo inversion
def monte_carlo_inversion(cdf_func, params, num_samples):
    samples = []
    for _ in range(num_samples):
        u = np.random.rand()
        sample = 0
        while cdf_func(sample, *params) < u:
            sample += 0.01  # Adjust the step size for better accuracy
        samples.append(sample)
    return samples

# Generate random samples from the Poisson distribution
num_samples = 1000
poisson_samples = monte_carlo_inversion(poisson_cdf, (lamda_poisson,), num_samples)

# Generate random samples from the Binomial distribution
binomial_samples = monte_carlo_inversion(binomial_cdf, (n_binomial, p_binomial), num_samples)

# Generate random samples from the Exponential distribution
exponential_samples = monte_carlo_inversion(exponential_cdf, (lamda_exponential,), num_samples)

# Plot histograms of the generated samples
plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
plt.hist(poisson_samples, bins=20, density=True, alpha=0.6, color='b', label='Poisson Samples')
plt.title('Poisson Distribution')
plt.xlabel('Value')
plt.ylabel('Probability')
plt.legend()

plt.subplot(1, 3, 2)
plt.hist(binomial_samples, bins=20, density=True, alpha=0.6, color='g', label='Binomial Samples')
plt.title('Binomial Distribution')
plt.xlabel('Value')
plt.ylabel('Probability')
plt.legend()

plt.subplot(1, 3, 3)
plt.hist(exponential_samples, bins=20, density=True, alpha=0.6, color='r', label='Exponential Samples')
plt.title('Exponential Distribution')
plt.xlabel('Value')
plt.ylabel('Probability')
plt.legend()

plt.tight_layout()
plt.show()
