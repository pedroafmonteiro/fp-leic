import math
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

formula1 = (-b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
formula2 = (-b - math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)

formula1r = round(formula1,2)
formula2r = round(formula2,2)

print("The solutions are {} and {}" .format(formula1r,formula2r))