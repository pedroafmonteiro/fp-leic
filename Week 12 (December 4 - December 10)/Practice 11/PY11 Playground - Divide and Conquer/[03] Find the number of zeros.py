def count_zeros(f):
    alist = f()
    num = 0
    for i in alist:
        if i == 0:
            num += 1
    return num