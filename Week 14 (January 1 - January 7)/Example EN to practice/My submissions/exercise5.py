def generate(word):
    results = set()
    if word.endswith('I'):
        results.add(word + 'U')
    if word.startswith('M'):
        results.add(word + word[1:])
    for i in range(len(word) - 2):
        if word[i:i+3] == 'III':
            results.add(word[:i] + 'U' + word[i+3:])
    for i in range(len(word) - 1):
        if word[i:i+2] == 'UU':
            results.add(word[:i] + word[i+2:])
    return sorted(list(results))