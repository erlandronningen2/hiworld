import datetime


def four2sixTimeDigit(item):
    t = item.split(":")
    hour, min = divmod(int(t[0]),60)
    t = datetime.time(hour, min, int(t[1]))
    return t

print(four2sixTimeDigit("91:50"))
print(four2sixTimeDigit("02:50"))
print(four2sixTimeDigit("55:50"))
print(four2sixTimeDigit("91:50"))
print(four2sixTimeDigit("02:50"))
print(four2sixTimeDigit("55:50"))
