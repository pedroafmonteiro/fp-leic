def sort_by_value(dict):
    list1 = []
    list2 = []
    for code in dict.values():
        list2.append(code)
    list2.sort()
    for i in list2:
        for color, code in dict.items():
            if code == i:
                tup = (color, code)
                list1.append(tup)
    return list1