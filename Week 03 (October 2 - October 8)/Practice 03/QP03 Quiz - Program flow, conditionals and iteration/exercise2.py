hours = int(input())
minutes = int(input())

if hours < 0 or hours > 23 or minutes < 0 or minutes > 59:
    print("INVALID DATE FORMAT")
else:
    if minutes == 0:
        if hours == 0:
            hours = "12"
            print(f'{hours} am')
        elif hours > 0 and hours < 12:
            hours = hours
            print(f'{hours} am')
        elif hours == 12:
            hours = hours
            print(f'{hours} pm')
        elif hours > 12 and hours < 24:
            hours = hours - 12
            print(f'{hours} pm')
    else:
        if hours == 0:
            hours = "12"
            minutes = str(minutes).zfill(2)
            print(f'{hours}:{minutes} am')
        elif hours > 0 and hours < 12:
            hours = hours
            minutes = str(minutes).zfill(2)
            print(f'{hours}:{minutes} am')
        elif hours == 12:
            hours = hours
            minutes = str(minutes).zfill(2)
            print(f'{hours}:{minutes} pm')
        elif hours > 12 and hours < 24:
            hours = hours - 12
            minutes = str(minutes).zfill(2)
            print(f'{hours}:{minutes} pm')