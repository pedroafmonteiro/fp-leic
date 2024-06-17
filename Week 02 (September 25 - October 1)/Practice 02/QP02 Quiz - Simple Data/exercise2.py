number = int(input("4-digit number: "))

thousands = str(number // 1000)
number = number % 1000
hundreds = str(number // 100)
number = number % 100
tens = str(number // 10)
ones = str(number % 10)

print(int(thousands + "000"))
print(int(hundreds + "00"))
print(int(tens + "0"))
print(int(ones))