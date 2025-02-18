import primes

p = primes.generatePrimeList(2000000)

d = {}

for i in p:
    d[i] = True

print "ready for calculation"

maxInRow = 0
maxProd = 0

for a in range(-999, 1000):
    for b in range(-1000, 1001):
        n = 0
        candidateMax = 1
        while True:
            N = n**2 + a*n + b
            #print "N: ", N
            if not d.has_key(N):
                if maxInRow < candidateMax:
                    maxInRow = candidateMax
                    maxProd = a * b
                    print "a: ", a, "b: ", b
                break
            candidateMax = candidateMax + 1
            n = n + 1

print "MaxProd: ", maxProd


