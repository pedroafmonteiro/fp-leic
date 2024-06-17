def rm_letter_rev(ch, s):
        if ch in s:
                s = s.replace(ch, '')
                s = s[::-1]
                return s
        else:
                s = s[::-1]
                return s