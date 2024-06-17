def x_union(list1, list2):
    map1 = list(map(lambda x: x[0], list1))
    map2 = list(map(lambda x: x[0], list2))
    
    filter1 = filter(lambda x: x[0] not in map2, list1)
    filter2 = filter(lambda x: x[0] not in map1, list2)
    result = list(filter1) + list(filter2)
    return result