def lfsr(n):
    result = ''
    n_copy = n[:]
    two_digits = n[-2:]
    if two_digits[0] != two_digits[1]:
        n = '1' + n
    else:
        n = '0' + n
    result += n[-1]
    n = n[:-1]
    while n != n_copy:
        two_digits = n[-2:]
        if two_digits[0] != two_digits[1]:
            n = '1' + n
        else:
            n = '0' + n
        result += n[-1]
        n = n[:-1]
    return result