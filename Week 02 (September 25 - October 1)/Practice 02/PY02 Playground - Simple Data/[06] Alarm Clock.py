hour = int(input("hour: "))
minutes = int(input("minutes: "))

total_minutes = hour * 60 + minutes

after_alarm = total_minutes + (6 * 60 + 51)

final_hours = after_alarm // 60
final_minutes = str(after_alarm % 60)

final_hours = str(final_hours % 24)

print(final_hours.zfill(2) + ":" + final_minutes.zfill(2))