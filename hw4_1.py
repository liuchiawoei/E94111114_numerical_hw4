import numpy as np

def integrand(x):
    return np.exp(x) * np.sin(4 * x)

a, b = 1, 2
h = 0.1
n = int((b - a) / h)

x_vals = np.linspace(a, b, n + 1)
y_vals = integrand(x_vals)

trapezoidal_result = (h / 2) * (y_vals[0] + 2 * np.sum(y_vals[1:-1]) + y_vals[-1])

if n % 2 == 0:
    simpson_result = (h / 3) * (
        y_vals[0] +
        4 * np.sum(y_vals[1:-1:2]) +
        2 * np.sum(y_vals[2:-2:2]) +
        y_vals[-1]
    )
else:
    simpson_result = None

midpoints = x_vals[1:-1:2]
midpoint_result = 2 * h * np.sum(integrand(midpoints))

print(f"(a) Composite Trapezoidal Rule: {trapezoidal_result}")
print(f"(b) Composite Simpson’s Rule:  {simpson_result}")
print(f"(c) Composite Midpoint Rule:    {midpoint_result}")