import numpy as np

a = 1
b = 2
n = 11  

h = (b - a) / (n - 1)

x = np.linspace(a, b, n)

f = np.exp(x) * np.sin(4 * x)

I_trap = (h / 2) * (f[0] + 2 * np.sum(f[1:n-1]) + f[-1])

print("Approximate integral using trapezoidal rule =", I_trap)
