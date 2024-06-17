def interleave(f1, f2):
    string = ''
    with open(f1, 'r') as file1:
        file1_content = file1.readlines()
    with open(f2, 'r') as file2:
        file2_content = file2.readlines()
    min_length = min(len(file1_content), len(file2_content))
    for n in range(min_length):
        string += file1_content[n]
        string += file2_content[n]
    return string