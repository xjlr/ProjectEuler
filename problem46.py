from sympy import isprime
#from sympy import is_square
from sympy.ntheory.primetest import is_square

candidate = 5
primes = [3] #except 2

def generate_more_primes():
    for p in range(primes[-1], candidate * 2, 2):
        if isprime(p):
#            print(p)
            primes.append(p)


def check_cadidate_goldback():
    if primes[-1] < candidate:
        generate_more_primes()
    
    for p in primes:
        if is_square((candidate-p)//2):
            return False
    return True

while True:
    if check_cadidate_goldback():
        print(candidate)
        break
    candidate += 2

