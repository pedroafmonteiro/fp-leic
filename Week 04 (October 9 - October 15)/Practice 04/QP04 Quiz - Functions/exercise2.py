def adigits(a, b, c):
    a = int(a)
    b = int(b)
    c = int(c)
    x = min(a, b, c)
    if x == a:
        y = min(b, c)
        if y == b:
            x *= 100
            y *= 10
            sum = x + y + c
        else:
            x *= 100
            y *= 10
            sum = x + y + b
    elif x == b:
        y = min(a, c)
        if y == a:
            x *= 100
            y *= 10
            sum = x + y + c
        else:
            x *= 100
            y *= 10
            sum = x + y + a
    elif x == c:
        y = min(a, b)
        if y == a:
            x *= 100
            y *= 10
            sum = x + y + b
        else:
            x *= 100
            y *= 10
            sum = x + y + a
    return sum