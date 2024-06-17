def sum_divisors(number):
    sum_divisors = 0
    for i in range(1, number):
        if number % i == 0:
            sum_divisors += i
    return sum_divisors

def check_friendly(number_one, number_two):
    """Check friendly numbers.

    >>> check_friendly(77, 77)
    'identical numbers: 77'
    >>> check_friendly(12, 55)
    'sum of divisors of 12 is not 55'
    >>> check_friendly(18, 21)
    'sum of divisors of 21 is not 18'
    >>> check_friendly(220, 284)
    '220 and 284 are friendly'

    >>> check_friendly(155,155)
    'identical numbers: 155'
    >>> check_friendly(100, 117)
    'sum of divisors of 117 is not 100'
    >>> check_friendly(43, 50)
    'sum of divisors of 43 is not 50'
    >>> check_friendly(17296,18416)
    '17296 and 18416 are friendly'
    """

    if number_one == number_two:
        return f'identical numbers: {number_one}'
    if sum_divisors(number_one) != number_two:
        return f'sum of divisors of {number_one} is not {number_two}'
    if sum_divisors(number_two) != number_one:
        return f'sum of divisors of {number_two} is not {number_one}'
    return f'{number_one} and {number_two} are friendly'
