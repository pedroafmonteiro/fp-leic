def last_man_standing(alist, step):
    if len(alist) == 1:
        return alist[0]
    else:
        del alist[step - 1]
        return last_man_standing(alist, step)

print(last_man_standing([3, 4, 1, 6, 2, 5, 7], 3))