import datetime


def four2sixTimeDigit(item):
    t = item.split(":")
    hour, min = divmod(int(t[0]),60)
    t = datetime.time(hour, min, int(t[1]))
    return t

print(four2sixTimeDigit("61:50"))
