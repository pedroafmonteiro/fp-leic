def time_diff(time1, time2):
    hours1, minutes1 = time1
    hours2, minutes2 = time2
    minutes_total1 = (hours1 * 60) + minutes1
    minutes_total2 = (hours2 * 60) + minutes2
    if minutes_total2 < minutes_total1:
        res = minutes_total1 - minutes_total2
        hours = res // 60
        minutes = res % 60
    else:
        res = minutes_total2 - minutes_total1
        hours = res // 60
        minutes = res % 60
    return (hours, minutes)