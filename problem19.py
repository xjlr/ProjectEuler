
def numberOfMonth(year, month):
    if month == 2:
        if year % 4 == 0:
            return 29
        else:
            return 28

    if month in [4,6,9,11]:
        return 30
    else:
        return 31

daysLeft = 0
sundays = 0
for y in range(1901, 2001):
    for m in range(1, 13):
        daysLeft = daysLeft + numberOfMonth(y, m)
        if daysLeft % 7 == 5:
            sundays = sundays + 1

print "Sundays: ", sundays
