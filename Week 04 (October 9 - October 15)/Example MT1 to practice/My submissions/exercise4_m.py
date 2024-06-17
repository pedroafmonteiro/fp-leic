def check_friendly(number_one, number_two):
    if number_one == number_two:
        return f'identical numbers: {number_one}'
    divisor_one = sum(i for i in range(1, number_one) if number_one % i == 0)
    divisor_two = sum(i for i in range(1, number_two) if number_two % i == 0)
    if divisor_one != number_two or divisor_two != number_one:
        return f'sum of divisors of {number_one} is not {number_two}' if divisor_one != number_two else f'sum of divisors of {number_two} is not {number_one}'
    return f'{number_one} and {number_two} are friendly'
