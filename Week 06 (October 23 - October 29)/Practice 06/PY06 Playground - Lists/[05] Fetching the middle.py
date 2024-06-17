def fetch_middle(llists):
    finallist = []
    for lists in llists:
        if len(lists) % 2 == 0:
            i = len(lists) // 2
            middle = (lists[i - 1] + lists[i]) / 2
            finallist.append(middle)
        else:
            i = round(len(lists) // 2)
            middle = lists[i]
            finallist.append(middle)
    return finallist