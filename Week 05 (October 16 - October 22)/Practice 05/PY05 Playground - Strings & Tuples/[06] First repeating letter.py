def repeated_letter(s):
    for i in s:
        if s.count(i) > 1:
            return i