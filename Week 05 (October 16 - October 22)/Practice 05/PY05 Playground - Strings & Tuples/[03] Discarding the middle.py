def discard_middle(s):
    if len(s) <= 3:
        return ''
    else:
        return s[0] + s[1] + s[-2] + s[-1]