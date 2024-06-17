def change(amount):
    coins = [200, 100, 50, 20, 10, 5, 2, 1]
    coins_used = []
    for coin in coins:
        while amount >= coin:
            coins_used.append(coin)
            amount -= coin
    return coins_used