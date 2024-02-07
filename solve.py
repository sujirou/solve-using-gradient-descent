#
# solve x⁵ + x = 3
#
def gradient_descent(x, alpha, num_iterations):
    for _ in range(num_iterations):
        gradient = 5 * x**4 + 1
        x = x - alpha * gradient
    return x

# Initial guess for x
x_initial = 1.0
# Learning rate
alpha = 0.01
# Number of iterations
num_iterations = 1000

# Solve the equation using gradient descent
solution = gradient_descent(x_initial, alpha, num_iterations)

print("Solution:", solution)
