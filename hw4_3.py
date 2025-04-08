import numpy as np
from scipy.integrate import dblquad

def integrand(x, y):
    return 2 * y * np.sin(x) + np.cos(x)**2

exact_value, _ = dblquad(lambda y, x: 2 * y * np.sin(x) + np.cos(x)**2, 0, np.pi / 4, lambda x: np.sin(x), lambda x: np.cos(x))

def simpsons_double_integral(func, a, b, n, m):
    x_vals = np.linspace(a, b, n + 1)
    hx = (b - a) / n
    total_integral = 0

    for i, xi in enumerate(x_vals):
        wx = 1 if i == 0 or i == n else (4 if i % 2 == 1 else 2)

        y_lower = np.sin(xi)
        y_upper = np.cos(xi)
        y_vals = np.linspace(y_lower, y_upper, m + 1)
        hy = (y_upper - y_lower) / m
        inner_integral = 0

        for j, yj in enumerate(y_vals):
            wy = 1 if j == 0 or j == m else (4 if j % 2 == 1 else 2)
            inner_integral += wy * func(xi, yj)

        total_integral += wx * (hy / 3) * inner_integral

    return (hx / 3) * total_integral

def gaussian_double_integral(func, a, b, n):
    nodes, weights = np.polynomial.legendre.leggauss(n)
    result = 0

    for i in range(n):
        xi = 0.5 * (b - a) * nodes[i] + 0.5 * (b + a)
        wi = weights[i]

        y_lower = np.sin(xi)
        y_upper = np.cos(xi)
        inner_result = 0

        for j in range(n):
            yj = 0.5 * (y_upper - y_lower) * nodes[j] + 0.5 * (y_upper + y_lower)
            wj = weights[j]
            inner_result += wj * func(xi, yj)

        result += wi * (y_upper - y_lower) / 2 * inner_result

    return (b - a) / 2 * result

simpson_result = simpsons_double_integral(integrand, 0, np.pi / 4, 4, 4)
gauss_result = gaussian_double_integral(integrand, 0, np.pi / 4, 3)

print(f"(a) Simpson's Rule (n=4, m=4):        {simpson_result}")
print(f"(b) Gaussian Quadrature (n=3, m=3):   {gauss_result}")
print(f"(c) The Exact Value:                  {exact_value}")
print(f"    Error of Simpson's Rule:          {abs(simpson_result - exact_value)}")
print(f"    Error of Gaussian Quadrature:     {abs(gauss_result - exact_value)}")