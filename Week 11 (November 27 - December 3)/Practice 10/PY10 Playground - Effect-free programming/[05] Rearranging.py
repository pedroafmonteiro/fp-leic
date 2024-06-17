def rearrange(l):
    non_positive = [x for x in l if x <= 0]
    positive = [x for x in l if x > 0]
    return non_positive + positive