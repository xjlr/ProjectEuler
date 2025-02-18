import math

digits = range(0,10)
digits.reverse()

def bestFitDigit(tailSize, threshold):
    f = math.factorial(tailSize)

    for pos in range(9, -1, -1):
        #print "pos*f == ", pos*f
        #print "threshold: ", threshold
        if pos * f < threshold:
            #print "Pos: ", pos
            return (pos, digits[len(digits) - 1 - pos])

    #print "should not happened"
    return (-1, -1)

t = 1000000

for n in range(9, 0, -1):
    (p, d) = bestFitDigit(n, t)
    digits.remove(d)
    t = t - p * math.factorial(n)
    print d
print digits[0]
