def sparse_dot_product(dict1, dict2):
    res = 0
    for keys1 in dict1.keys():
        for keys2 in dict2.keys():
            if keys1 == keys2:
                res += dict1[keys1]*dict2[keys2]
    return res