def digits_average(n):
    while n >= 10:
        digits = []
        while n > 0:
            digits.append(n % 10)
            n //= 10
        digits.reverse()
        n = sum(digits[i] + digits[i+1] for i in range(len(digits)-1))
        n = -(-n // 2)
    return n
