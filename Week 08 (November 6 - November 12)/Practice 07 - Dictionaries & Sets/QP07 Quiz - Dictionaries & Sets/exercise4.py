def isomorphic(astring1, astring2):
    dict1 = {}
    dict2 = {}
    for i in range(len(astring1)):
        dict1[astring1[i]] = astring2[i]
        dict2[astring2[i]] = astring1[i]
    if len(dict1) == len(dict2):
        return f"'{astring1}' and '{astring2}' are isomorphic"
    else:
        return f"'{astring1}' and '{astring2}' are not isomorphic"