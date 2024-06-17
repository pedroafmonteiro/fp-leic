def local_minima(alist):
    new_list = []
    for i in range(len(alist) - 2):
        sub = alist[i:i + 3]
        minimum = min(sub)
        c = sub.count(minimum)
        if c == 1:
            new_list.append(minimum)
    return new_list