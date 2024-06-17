def fight(heroes, villain):
    for heroe in heroes:
        if heroe['category'] == villain['category']:
            if heroe['health'] >= villain['health']:
                heroe['score'] += 1
                name = heroe['name']
                score = heroe['score']
                return f'{name} defeated the villain and now has a score of {score}'
            else:
                villain['health'] -= (heroe['health'] / 2)
                name = villain['name']
                health = villain['health']
    return f'{name} prevailed with {health}HP left'