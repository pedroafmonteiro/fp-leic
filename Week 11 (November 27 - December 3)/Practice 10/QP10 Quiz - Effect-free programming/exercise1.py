def square_odds(values):
    alist = values.split(',')
    final = [int(x) * int(x) for x in alist if int(x) % 2 != 0]
    final2 = ','.join(map(str,final))
    return final2