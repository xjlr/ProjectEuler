
def isAbundant(num):
    sum = 0
    for n in range(num/2, 0, -1):
        if num % n == 0:
            sum = sum + n
        if sum > num:
            return True
    return False

def isSumExist(num):
    low = 0
    hi = len(abundantNumbers) - 1

    while (low <= hi):
        if abundantNumbers[low] + abundantNumbers[hi] == num:
            True
        elif abundantNumbers[low] + abundantNumbers[hi] < num:
            low = low + 1
        else:
            hi = hi - 1
    return False


abundantNumbers = []

for trial in range(12, 28124):
    if isAbundant(trial):
        abundantNumbers.append(trial)

sum = 0
d = {}

for n1 in abundantNumbers:
    for n2 in abundantNumbers:
        d[n1+n2] = True

for n in range(1, 28124):
    if not n in d.keys():
        sum = sum + n

print "dict size: ", len(d)

print "Sum: ", sum

"""
for n in range(0, 28124):
    if not isSumExist(n):
        sum = sum + n
    if n % 10 == 0:
        print "progress: ", n

#print abundantNumbers
print "Sum : ", sum
"""

