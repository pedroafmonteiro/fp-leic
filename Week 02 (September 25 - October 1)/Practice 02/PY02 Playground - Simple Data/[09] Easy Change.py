price = int(input("Price: "))
received = int(input("Amount received: "))

difference = received - price
difference1 = str(difference // 50)
difference %= 50
difference2 = str(difference // 20)
difference %= 20
difference3 = str(difference // 10)
difference %= 10
difference4 = str(difference // 5)


print(" ".join([difference1, difference2, difference3, difference4]))