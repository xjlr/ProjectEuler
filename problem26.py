
def numberOfDecimalRepresentation(n):
    decimals = [(0, 1)] # (value, modulo)
    while True:
        shouldDiv = decimals[-1][1] * 10
        value = shouldDiv / n
        modulo = shouldDiv % n
        if modulo == 0:
            return 0
        t = (value, modulo)
        try:
            idx = decimals.index(t)
            return len(decimals) - idx
        except ValueError:
            decimals.append(t)


print "3 value: ", numberOfDecimalRepresentation(3)
print "2 value: ", numberOfDecimalRepresentation(2)
print "6 value: ", numberOfDecimalRepresentation(6)
print "7 value: ", numberOfDecimalRepresentation(7)
print "9 value: ", numberOfDecimalRepresentation(9)
print "999 value: ", numberOfDecimalRepresentation(999)

maxLong = 0
maxNumber = 0
for n in range(2, 1000):
    l = numberOfDecimalRepresentation(n)
    if maxLong < l:
        maxLong = l
        maxNumber = n

print "Number: ", maxNumber
print "Long: ", maxLong

