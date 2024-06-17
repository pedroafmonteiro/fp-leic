pe1 = int(input())
pe2 = int(input())
pe3 = int(input())
pe4 = int(input())

pe3_4 = max(pe3, pe4)
if pe3_4 >= 40:
    pe = (pe1+pe2+pe3_4 - min(pe1, pe2, pe3_4)) / 2
    print(round(pe))
else:
    print("RFF")

"""
# public tests:
80, 70, 50, 0 => 75
80, 60, 35, 50 => 70
100, 100, 35, 35 => RFF
30, 50, 40, 0 => 45

# private tests:
70, 60, 50, 0 => 65
100, 100, 80, 0 => 100
100, 100, 39, 0 => RFF
80, 60, 35, 50 => 70
"""
