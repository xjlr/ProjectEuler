
def sumdigitpow(n):
    sum = 0
    while n:
        d = n % 10
        sum = sum + d**5
        n = n / 10
    return sum

sum = 0
for n in range(2, 360000):
    if sumdigitpow(n) == n:
        sum = sum + n
        print "n: ", n

print "Sum: ", sum
