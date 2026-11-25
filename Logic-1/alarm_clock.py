def alarm_clock(day, vacation):
    if (vacation and (day==6 or day==0)):
        return "off"
    elif (vacation and 0<=day<=5) or (day==6 or day==0):
        return "10:00"
    else:
        return "7:00"

print(alarm_clock(5, True))
print(alarm_clock(6, True))
print(alarm_clock(0, True))
print(alarm_clock(5, False))
print(alarm_clock(1, True))
print(alarm_clock(0, False))