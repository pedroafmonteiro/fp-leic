def biggest_member(atuple):
    if len(atuple) == 1:
        return atuple
    else:
        alist = [zip(i, atuple) for i in atuple]
        return alist
                    

print(biggest_member((1, (5, (6, 8), 3, 9), 2)))