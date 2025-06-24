import math

def generatePrimeList(n):
    primes = [2]
    N = 3
    while primes[-1] < n:
        square = (int)(math.sqrt(N))
        for p in primes:
            if N % p == 0:
                break
            if p > square:
                primes.append(N)
                break
        N += 2

    return primes


#l = generatePrimeList(42)

#print l

