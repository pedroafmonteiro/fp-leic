def permutations(str):
    if len(str) <= 1:
        return [str]
    result = []
    for i, char in enumerate(str):
        remaining_chars = str[:i] + str[i+1:]
        sub_permutations = permutations(remaining_chars)
        for perm in sub_permutations:
            result.append(char + perm)
    return result