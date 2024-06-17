a = int(input("Number a: "))
b = int(input("Number b: "))

difference = a - b
result = (a + b) * (1 + (difference % 2 == 0)) + (a * b) * (difference % 2 != 0)

print(result)