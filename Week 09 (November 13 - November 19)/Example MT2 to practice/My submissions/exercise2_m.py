def isPrime(n):
    for x in range(2, n):
        if n % x == 0:
            return False
    return True

def next_prime(number):
    next = number + 1
    while True:
        if (isPrime(next)):
            return next
        next += 1