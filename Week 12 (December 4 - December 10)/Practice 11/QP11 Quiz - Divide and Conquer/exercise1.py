def merge(xs, ys):
    result = []
    i = j = 0
    while i < len(xs) and j < len(ys):
        if xs[i] < ys[j]:
            result.append(xs[i])
            i += 1
        else:
            result.append(ys[j])
            j += 1

    # Add the remaining elements from both lists, if any
    result.extend(xs[i:])
    result.extend(ys[j:])

    return result

def msort(xs):
    if len(xs) == 1 or len(xs) == 0:
        return xs
    else:
        middle_index = len(xs) // 2
        ys = xs[middle_index:]
        xs = xs[:middle_index]
        ys = msort(ys)
        xs = msort(xs)
        return merge(xs, ys)
