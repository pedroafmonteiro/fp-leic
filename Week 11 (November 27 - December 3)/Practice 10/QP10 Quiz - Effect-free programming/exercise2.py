def comprehensions(i, j):
    numbers = [x for x in range(i, j + 1) if x % 10 == 3 or x % 10 == 8]
    square_root = [round(x ** (1/2), 2) for x in range(i, j + 1)]
    square_root = tuple(square_root)
    ascii_table = {num: chr(num) for num in range(i, j + 1)}
    return numbers, square_root, ascii_table