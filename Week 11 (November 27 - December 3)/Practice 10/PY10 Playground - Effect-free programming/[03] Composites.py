def is_composite(n):
    for i in range(2, int(n/2)+1):
        if (n % i) == 0:
            return True
    return False

def get_composites(n):
    for i in range(2, n + 1):
        if is_composite(i):
            yield i
