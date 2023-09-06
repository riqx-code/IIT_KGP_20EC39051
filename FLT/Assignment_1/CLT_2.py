import numpy as np
import matplotlib.pyplot as plt

# Define the box function B(x)
def box_function(x):
    return np.where(np.logical_and(x >= -1, x <= 1), 1, 0)

# Define the interval and x values for plotting
x = np.linspace(-5, 5, 1000)

# Convolve the box function with itself n times and plot
n_values = [2, 3, 4, 5, 6, 7, 8, 9, 10]

plt.figure(figsize=(12, 8))

for n in n_values:
    convolved_y = box_function(x)
    for _ in range(n - 1):
        convolved_y = np.convolve(convolved_y, box_function(x), mode='same') / len(x)
    plt.plot(x, convolved_y, label=f'n = {n}')

plt.xlabel('x')
plt.ylabel('Convolved Function')
plt.title('Repetitive Convolution of B(x) with Itself')
plt.legend()
plt.grid(True)
plt.xlim(-2, 2)
plt.ylim(0, 1.2)
plt.show()
