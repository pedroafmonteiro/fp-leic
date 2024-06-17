def longest_prefix(words):
    if len(words) == 1:
        return words[0]
    else:
        middle_index = len(words) // 2
        half1 = words[:middle_index]
        half2 = words[middle_index:]
        prefix1 = longest_prefix(half1)
        prefix2 = longest_prefix(half2)
        return common_prefix(prefix1, prefix2)

def common_prefix(prefix1, prefix2):
    i = 0
    while i < len(prefix1) and i < len(prefix2) and prefix1[i] == prefix2[i]:
        i += 1
    return prefix1[:i]
