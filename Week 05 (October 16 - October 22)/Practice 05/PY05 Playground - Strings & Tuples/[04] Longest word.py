def longest(s):
    words = s.split()
    newlist = []
    for i in words:
        newlist.append(len(i))
    return max(newlist)