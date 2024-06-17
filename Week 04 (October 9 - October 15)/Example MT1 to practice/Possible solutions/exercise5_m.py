def validate_cc(number):
    """Validate a credit card number.

    >>> print(validate_cc(4028743156781887))
    Card number 4028743156781887 valid
    >>> print(validate_cc(4012888888881882))
    Card number 4012888888881882 invalid (checksum 1)
    >>> print(validate_cc(4712812834781881))
    Card number 4712812834781881 valid
    >>> print(validate_cc(4712818234781881))
    Card number 4712818234781881 invalid (checksum 7)

    >>> print(validate_cc(4632818234512773))
    Card number 4632818234512773 valid
    >>> print(validate_cc(4623818234512773))
    Card number 4623818234512773 invalid (checksum 9)
    >>> print(validate_cc(4413813434932173))
    Card number 4413813434932173 valid
    >>> print(validate_cc(4413613434932173))
    Card number 4413613434932173 invalid (checksum 6)
    """

    total = 0
    i = 0
    n = number
    while n > 0:
        digit = n % 10
        if i % 2 == 0:
            parcel = digit
        else:
            parcel = 2*digit
        total = total + (parcel % 10) + (parcel//10)
        i = i+1
        n = n//10

    if total % 10 == 0:
        return f"Card number {number} valid"
    else:
        return f"Card number {number} invalid (checksum {total%10})"
