def sum_numbers(number):
    sumnum = 0
    for i in range(1, number + 1):
        sumnum += (i - (sum(range(1, number + 1)) / number)) ** 2
    return sumnum


def var_numbers(number, precision=2):
    res = sum_numbers(number) / number
    return round(res, precision)