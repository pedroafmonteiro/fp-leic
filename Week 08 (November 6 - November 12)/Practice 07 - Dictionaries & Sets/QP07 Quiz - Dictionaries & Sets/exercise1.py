def switch_dict(adict):
    ndict = {}
    for (x,y) in adict.items():
        if y in ndict:
            ndict[y].append(x)
        else:
            ndict[y] = [x]
    return ndict