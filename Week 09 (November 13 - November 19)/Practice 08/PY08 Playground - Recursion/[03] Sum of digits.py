def sum_digits_rec(n):
    if n < 10:
        return n
    else:
        first_digit = n // (10 ** (len(str(n)) - 1))
        remaining_digits = n % (10 ** (len(str(n)) - 1))
        return first_digit + sum_digits_rec(remaining_digits)