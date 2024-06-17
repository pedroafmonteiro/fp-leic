from functools import reduce

def bounding_box(pts):
    x_coords = list(map(lambda pt: pt[0], pts))
    y_coords = list(map(lambda pt: pt[1], pts))
    
    xmin = reduce(lambda a, b: a if a < b else b, x_coords)
    ymin = reduce(lambda a, b: a if a < b else b, y_coords)
    xmax = reduce(lambda a, b: a if a > b else b, x_coords)
    ymax = reduce(lambda a, b: a if a > b else b, y_coords)
    
    return (xmin, ymin, xmax, ymax)