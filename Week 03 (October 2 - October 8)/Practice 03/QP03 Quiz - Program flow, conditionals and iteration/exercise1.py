num = int(input())

for index in range(1,11):
    if num == index:
        res = num ** 2
        s = f'{num} ^ 2 = {res}'
        print(s)
        break
    res = num * index
    s = f'{num} x {index} = {res}'
    print(s)
