def days_until_christmas(date):
    res = 0
    days_of_month = {
        1: 31,
        2: 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }
    day, month, year = date
    if day > 25 and month == 12:
        res += 31 - day
        res += 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30 + 25
        return res
    elif day == 25 and month == 12:
        return 0
    elif day < 25 and month == 12:
        return 25 - day
    else:
        res += days_of_month[month] - day
        for months in days_of_month.keys():
            if months > month:
                res += days_of_month[months]
        res -= 6
        return res