import string

def count_chars(a_string):
    alphabetic = 0
    digits = 0
    special = 0
    for i in a_string:
        if i in string.ascii_letters:
            alphabetic += 1
        elif i in string.digits:
            digits += 1
        elif i in string.punctuation:
            special += 1
    return (alphabetic, digits, special)