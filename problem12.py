import math
import numpy

N = 3

primes = [2]

def numberOfDivision(number):
    count = 0
    for i in range(1, number + 1):
        if N % i == 0:
            count = count + 1
    return count

def numberOfDivisionFast(number):
    primeFactors = []
    for p in primes:
        div = p
        factor = 0
        found = False
        while div <= number:
            if number % div == 0:
                found = True
                factor = factor + 1
            div = div * p
        if found:
            primeFactors.append(factor + 1)

    return numpy.prod(primeFactors)



while primes[-1] < 100:
    square = (int)(math.sqrt(N))
    for p in primes:
        if N % p == 0:
            break
        if p > square:
            primes.append(N)
            break
    N = N + 2

print "#primes created: ", primes
SUM = 0

print "#3: ", numberOfDivisionFast(3)
print "#10: ", numberOfDivisionFast(10)
print "#15: ", numberOfDivisionFast(15)
print "#21: ", numberOfDivisionFast(21)
print "#28", numberOfDivisionFast(28)
N = 2
while True:
    N = N + 1
    SUM = N*(N + 1)/2
    if numberOfDivisionFast(SUM) >= 500:
        break;

print "SUM: ", SUM
print "N: ", N

