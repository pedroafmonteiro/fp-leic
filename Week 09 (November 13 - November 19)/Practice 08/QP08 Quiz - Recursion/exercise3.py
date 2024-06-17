def max_path(tree):
    if type(tree) == int:
        return tree
    else:
        left_path = max_path(tree[0])
        right_path = max_path(tree[2])
        return tree[1] + max(left_path, right_path)