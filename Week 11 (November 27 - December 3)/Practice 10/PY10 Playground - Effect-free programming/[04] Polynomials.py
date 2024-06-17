def evaluate(a, x):
    alist = [i * (x ** a.index(i)) for i in a]
    res = sum(alist)
    return res