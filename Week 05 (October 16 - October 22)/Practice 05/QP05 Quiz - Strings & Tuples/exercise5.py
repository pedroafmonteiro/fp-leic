def triplet(tup):
    for i in range(len(tup)):
        for i2 in range(len(tup)):
            for i3 in range(len(tup)):
                if (i != i2 and i != i3 and i2 != i3) and tup[i] + tup[i2] + tup[i3] == 0:
                    return (tup[i], tup[i2], tup[i3])
    return ()