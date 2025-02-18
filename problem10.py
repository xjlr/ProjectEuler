import math

primes = [2, 3, 5, 7]

N = 9
while primes[-1] < 2000000:
    square = (int)(math.sqrt(N))
    for p in primes:
        if N % p == 0:
            break
        if p > square:
            primes.append(N)
            break
    N = N + 2

print primes

print "-------"

print sum(primes[:-1])


