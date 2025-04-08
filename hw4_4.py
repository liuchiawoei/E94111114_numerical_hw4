import math

def composite_simpson_1d(func, a, b, n):
    if n % 2 != 0 or n <= 0:
        return float('nan')
    h = (b - a) / n
    sum_val = func(a) + func(b)
    for i in range(1, n, 2):
        sum_val += 4.0 * func(a + i * h)
    for i in range(2, n - 1, 2):
        sum_val += 2.0 * func(a + i * h)
    return (h / 3.0) * sum_val

def func_a(x):
    if x == 0.0:
        return 0.0
    if x < 0.0:
        return float('nan')
    return math.pow(x, -0.25) * math.sin(x)

def func_b_transformed(t):
    if t == 0.0:
        return 0.0
    if t < 0.0:
        return float('nan')
    return t * t * math.sin(1.0 / t)

if __name__ == "__main__":
    n = 4
    result_a = composite_simpson_1d(func_a, 0.0, 1.0, n)
    result_b = composite_simpson_1d(func_b_transformed, 0.0, 1.0, n)

    if not math.isnan(result_a):
        print(f"Approximate value of (a): {result_a:.10f}")
    if not math.isnan(result_b):
        print(f"Approximate value of (b): {result_b:.10f}")