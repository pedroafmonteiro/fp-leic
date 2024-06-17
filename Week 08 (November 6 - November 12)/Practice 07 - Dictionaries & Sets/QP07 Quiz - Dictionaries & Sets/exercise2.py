def roman_to_integer(astring):
    sum = 0
    romans = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    for i in range(len(astring) - 1):
        current = astring[i]
        next = astring[i + 1]
        c_value = romans[current]
        n_value = romans[next]
        if n_value > c_value:
            sum -= c_value
        else:
            sum += c_value
    last_digit = astring[-1]
    l_value = romans[last_digit]
    sum += l_value
    return sum