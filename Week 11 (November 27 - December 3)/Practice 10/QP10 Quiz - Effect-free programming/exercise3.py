def pythagoreans(a, b):
    return [(x, y, z) for x in range(a, b) for y in range(x + 1, b) for z in range(y + 1, b) if x**2 + y**2 == z**2]
