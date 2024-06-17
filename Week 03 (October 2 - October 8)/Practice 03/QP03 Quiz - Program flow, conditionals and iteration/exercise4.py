num = int (input())
str1 = "#"

for element in range (num):
    a = (f"{num * str1}")

first_lines = int((num - 2) / 2)
first_lines_odds = int((num - 1) / 2)

b = 0
c = 0
d = 0

e = 0
f = 0
g = 0

if len(a) % 2 == 0:
    while b < first_lines:
        print(a)
        b = b + 1
    while c < (num - (2 * first_lines)):
        line_centre = (f"{first_lines * str1}00{first_lines * str1}")
        print(line_centre)
        c = c + 1
    while d < first_lines:
        print(a)
        d = d + 1

if len(a) % 2 != 0:
    while e < first_lines_odds:
        print(a)
        e = e + 1
     
    line_centre_odds = (f"{first_lines_odds * str1}0{first_lines_odds * str1}" )
    print(line_centre_odds)
        
    while g < first_lines_odds:
        print(a)
        g = g + 1