def juggler(n, p):
    if p == 0:
        return n
    else:
        if juggler(n, p - 1) % 2 == 0:
            res = int(juggler(n, p - 1) ** (1/2))
        else:
            res = int(juggler(n, p - 1) ** (3/2))
    return res