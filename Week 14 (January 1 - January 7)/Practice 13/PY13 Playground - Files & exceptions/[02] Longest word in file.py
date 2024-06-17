def longest(filename):
    with open(filename, "r") as file:
        content = file.read().split()
    max_len = len(max(content, key=len))
    list = [word for word in content if len(word) == max_len]
    return list[0]