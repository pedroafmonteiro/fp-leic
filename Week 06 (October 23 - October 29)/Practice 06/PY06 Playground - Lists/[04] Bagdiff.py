def bagdiff(xs, ys):
    for i in ys:
        if i in xs:
            xs.remove(i)
    return xs