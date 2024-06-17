def most_frequent(alist):
    freq_dict = {}
    newlist = []
    for i in alist:
        freq_dict[i] = freq_dict.get(i, 0) + 1
    for key, value in freq_dict.items():
        if value == max(freq_dict.values()):
            newlist.append(key)
    return max(newlist)