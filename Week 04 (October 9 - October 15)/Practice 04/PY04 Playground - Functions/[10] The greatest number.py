def greatest(num):
    num = str(num)
    digits = sorted(num, reverse=True)
    result = int(''.join(digits))
    return result