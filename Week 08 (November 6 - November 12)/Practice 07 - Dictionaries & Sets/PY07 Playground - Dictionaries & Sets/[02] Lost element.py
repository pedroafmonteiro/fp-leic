def lost_element(s1, s2):
    if len(s1) > len(s2):  
        for i in s2:
            s1.discard(i)
        return s1.pop()
    else:
        for i in s1:
            s2.discard(i)
        return s2.pop()