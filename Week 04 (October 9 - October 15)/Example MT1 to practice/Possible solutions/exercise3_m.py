import math

def approx_cos(x, n):
    '''Approximate cos by the Taylor series of degree 2n.

    >>> approx_cos(1.0, 3)
    0.54167
    >>> approx_cos(2.0, 3)
    -0.33333
    >>> approx_cos(1.0, 5)
    0.5403
    >>> approx_cos(-1.0, 10)
    0.5403

    >>> approx_cos(0.5, 3)
    0.8776
    >>> approx_cos(1.0, 4)
    0.54028
    >>> approx_cos(-0.5, 5)
    0.87758
    >>> approx_cos(-2.0, 10)
    -0.41615
    '''

    s = 0.0
    for i in range(n):
        s = s + (-1)**i / math.factorial(2*i) * x**(2*i)
    return round(s, 5)

# alternative (strength reduction)
def approx_cos_alt(x, n):
    s = 0.0
    fact = 1.0
    power = 1.0
    for i in range(n):
        s = s + power/fact
        power = - power * x*x
        fact = fact * (2*i+1) * (2*i+2)
    return round(s, 5)
