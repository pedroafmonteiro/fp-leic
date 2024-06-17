def bubble_sort(alist):
    b_list = alist.copy()
    n = len(b_list)
    swapped = True

    while swapped:
        swapped = False
        for i in range(n - 1):
            if b_list[i] > b_list[i + 1]:
                b_list[i], b_list[i + 1] = b_list[i + 1], b_list[i]
                swapped = True

    return b_list