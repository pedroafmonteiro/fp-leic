def evaluate(a, x):
    return sum(map(lambda y: y * (x ** a.index(y)), a))

