import itertools
import math
from primes import generatePrimeList

primes_list = generatePrimeList(int(math.sqrt(87654322)))

#print(len(p))
# Generate all permutations of the digits 1 to 8
for perm in itertools.permutations(range(7, 0, -1)):
    # Convert the tuple to a single number
    number = int(''.join(map(str, perm)))
    is_prime = True
    for p in primes_list:
        if number % p == 0:
            is_prime = False
            break
    if is_prime:
        print(number)
        break
    
    #print(number)

#prim = generatePrimeList(int(math.sqrt(87654322)))