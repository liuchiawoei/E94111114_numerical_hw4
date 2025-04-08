import numpy as np
import scipy.integrate as spi

def original_function(x):
    return x**2 * np.log(x)

def transformed_function(t):
    x = 0.25 * t + 1.25
    return 0.25 * x**2 * np.log(x)

nodes3, weights3 = np.polynomial.legendre.leggauss(3)
gauss_result_3 = np.sum(weights3 * transformed_function(nodes3))

nodes4, weights4 = np.polynomial.legendre.leggauss(4)
gauss_result_4 = np.sum(weights4 * transformed_function(nodes4))

exact_value, _ = spi.quad(original_function, 1, 1.5)

print(f"Gaussian Quadrature (n=3): {gauss_result_3}")
print(f"Absolute Error:            {abs(gauss_result_3 - exact_value)}")
print(f"Gaussian Quadrature (n=4): {gauss_result_4}")
print(f"Absolute Error:            {abs(gauss_result_4 - exact_value)}")
print(f"Exact Integral Value:      {exact_value}")