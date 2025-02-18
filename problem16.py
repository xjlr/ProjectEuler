N = 2**1000

def sumDigits(num):
    l = []
    while num:
        l.append(num % 10)
        num = num / 10

    return sum(l)

print "N: ", sumDigits(N)
