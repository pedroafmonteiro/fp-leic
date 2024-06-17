def summary_ranges(a_string):
    a_string = a_string.replace(',', ' ')
    return list(a_string.strip())

print(summary_ranges('0,1,2,3,4,5,7,10,11,20,21'))