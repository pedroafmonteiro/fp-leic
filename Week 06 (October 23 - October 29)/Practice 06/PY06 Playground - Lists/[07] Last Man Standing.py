def last_man_standing(a_list, step):
    circle = a_list.copy()
    index = 0
    while len(circle) > 1:
        index = (index + step - 1) % len(circle)
        circle.pop(index)
    return circle[0]

print(last_man_standing([3, 4, 1, 6, 2, 5, 7], 3))