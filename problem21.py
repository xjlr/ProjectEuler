
def sumOfProperDivisors(num):
    s = 0
    for i in range(1, num / 2 + 1):
        if num % i == 0:
            s = s + i

    return s

dict = {}
s = 0
for i in range(2, 10000):
    dict[i] = sumOfProperDivisors(i)

for x in dict:
    if dict[x] == x:
        continue

    try:
        value = dict[x]
        if dict[value] == x:
            s = s + x
    except KeyError:
        continue


print "Sum: ", s
print "-----"
#print dict
