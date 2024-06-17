from itertools import combinations

def number_of_collisions(objects):
    pairs = list(combinations(objects, 2))
    count = 0

    def intersect(obj1, obj2):
        if obj1['x1'] > obj2['x2'] or obj1['x2'] < obj2['x1']:
            return False
        if obj1['y1'] > obj2['y2'] or obj1['y2'] < obj2['y1']:
            return False
        return True

    for a, b in pairs:
        if intersect(a, b):
            count += 1

    return count