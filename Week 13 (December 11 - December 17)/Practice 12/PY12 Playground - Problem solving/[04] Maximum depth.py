def maximum_depth(l):
    depths = []
    for item in l:
        if isinstance(item, list):
            depths.append(maximum_depth(item))
    if len(depths) > 0:
        return 1 + max(depths)
    return 1