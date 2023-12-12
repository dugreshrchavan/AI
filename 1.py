import matplotlib.pyplot as plt
import numpy as np

# Define the mathematical function
def objective_function(x):
    return -x**2 + 4*x

# Hill climbing algorithm
def hill_climbing(initial_x, step_size, num_steps):
    current_x = initial_x

    for _ in range(num_steps):
        # Evaluate the current and neighboring points
        current_value = objective_function(current_x)
        next_value = objective_function(current_x + step_size)

        # If the neighboring point has a higher value, move to that point
        if next_value > current_value:
            current_x += step_size
        else:
            break  # Stop if no improvement is found

    return current_x

# Set initial parameters
initial_x = 0.0
step_size = 0.1
num_steps = 100

# Run the hill climbing algorithm
result = hill_climbing(initial_x, step_size, num_steps)

# Print the result
print("Maximum found at x =", result)
print("Maximum function value =", objective_function(result))

# Plot the function
x_values = np.linspace(-2, 6, 100)
y_values = objective_function(x_values)

plt.plot(x_values, y_values, label='f(x) = -x^2 + 4x')
plt.scatter(result, objective_function(result), color='red', label='Maximum')
plt.title('Hill Climbing Algorithm')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.show()
