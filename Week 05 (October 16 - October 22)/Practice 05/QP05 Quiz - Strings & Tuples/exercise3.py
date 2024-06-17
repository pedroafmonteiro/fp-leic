def mask_data(data, n_characters, position):
    if n_characters == 0:
        return data
    else:
        if position == 'begin':
            data = data.replace(data[0:n_characters], '*' * n_characters)
            return data
        elif position == 'end':
            data = data.replace(data[len(data) - n_characters:len(data)], '*' * n_characters)
            return data