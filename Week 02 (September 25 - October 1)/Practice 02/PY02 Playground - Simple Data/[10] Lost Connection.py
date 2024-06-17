import math

def time_until_lost_connection(direction_A, direction_B):
    max_distance = 35/2
    angle = (abs(direction_B - direction_A)) / 2
    angle_radians = math.pi * angle / 180
    km_walked = max_distance / (math.sin(angle_radians))
    minutes_passed = km_walked*60 / 5

    return round(minutes_passed,3)