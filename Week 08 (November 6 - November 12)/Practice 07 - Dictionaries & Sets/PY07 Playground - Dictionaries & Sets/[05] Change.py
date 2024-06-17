def change(money):
    dict = {2.0: 0, 1.0: 0, 0.5: 0, 0.2: 0, 0.1: 0, 0.05: 0, 0.02: 0, 0.01: 0}
    tolerance = 0.0001
    for key in dict.keys():
        while money > key or abs(money - key) < tolerance:
            money -= key
            dict[key] += 1
    return dict