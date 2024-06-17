import math

def approx_cos(x, n):
    cos = 0
    for k in range(n):
        cos += (((-1) ** k) / math.factorial(2 * k)) * (x ** (2 * k))
    return round(cos, 5)