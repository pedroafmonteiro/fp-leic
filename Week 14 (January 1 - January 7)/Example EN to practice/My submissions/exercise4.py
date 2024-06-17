def list_paths(dirtree, parent_folder=""):
    paths = []
    file_folder, subtrees = dirtree
    current_folder = f"{parent_folder}/{file_folder}" if parent_folder else file_folder
    for i in range(0, len(subtrees)):
        if type(subtrees[i]) == str:
            paths.append(f'{current_folder}/{subtrees[i]}')
        elif type(subtrees[i]) == tuple:
            paths.extend(list_paths(subtrees[i], current_folder))
    return paths
