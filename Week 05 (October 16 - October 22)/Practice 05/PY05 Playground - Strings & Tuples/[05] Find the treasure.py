def map(pos, steps):
    steps = steps.replace('-', ' ')
    words = steps.split()
    for i in words:
        if i == 'up':
            pos = (int(pos[0]), (int(pos[-1]) + 1))
        elif i == 'down':
            pos = (int(pos[0]), (int(pos[-1]) - 1))
        elif i == 'left':
            pos = ((int(pos[0]) - 1), int(pos[-1]))
        elif i == 'right':
            pos = ((int(pos[0]) + 1), int(pos[-1]))
    return pos