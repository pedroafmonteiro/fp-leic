def variance(alist):
    average = sum(alist) / len(alist)
    up = map(lambda x: (x - average) ** 2, alist)
    variance = sum(up) / len(alist)
    return round(variance, 3)