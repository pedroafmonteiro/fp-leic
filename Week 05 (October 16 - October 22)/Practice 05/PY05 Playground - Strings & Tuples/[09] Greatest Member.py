import string

def greatest_member(a_tuple):
    list_values = []
    for i in a_tuple:
        res = 0
        for n in i:
            res += ord(n)
        list_values.append(res)
    return list_values

print(greatest_member(('hyde', 'jekyll')))