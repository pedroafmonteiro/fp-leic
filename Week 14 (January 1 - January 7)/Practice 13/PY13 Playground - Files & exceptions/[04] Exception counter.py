def count_exceptions(f, n1, n2):
    exceptions = 0
    for n in range(n1, n2 + 1):
        try:
            f(n)
        except:
            exceptions += 1
    return exceptions