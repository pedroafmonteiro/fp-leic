def academy_awards(alist):
    dict = {}
    for categories, movie in alist:
        dict[movie] = dict.get(movie, 0) + 1
    return dict