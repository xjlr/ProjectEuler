from primes import generatePrimeList
#from math import isprime
import sympy

primes_list = generatePrimeList(10000)

def is_prime_pair_set(p_set):
    for i in range(0, len(p_set)):
        for j in range(i + 1, len(p_set)):
            ij = int(str(primes_list[i]) + str(primes_list[j]))
            ji = int(str(primes_list[j]) + str(primes_list[i]))
            if not sympy.isprime(ij) or sympy.isprime(ji):
                return False
    return True

def is_prime_pair_set2(p_set, idx):
    for i in range(0, len(p_set)):
        ij = int(str(primes_list[p_set[i]]) + str(primes_list[idx]))
        ji = int(str(primes_list[idx]) + str(primes_list[p_set[i]]))

        if not sympy.isprime(ij) or not sympy.isprime(ji):
            return False
    return True

min_value = float('inf')

for i1 in range(1, len(primes_list)):
    l1 = [i1]
    for i2 in range(i1 + 1, len(primes_list)):
        if not is_prime_pair_set2(l1, i2):
            continue
        l2 = [i1, i2]
        for i3 in range(i2 + 1, len(primes_list)):
            if not is_prime_pair_set2(l2, i3):
                continue
            l3 = [i1, i2, i3]
            for i4 in range(i3 + 1, len(primes_list)):
                if not is_prime_pair_set2(l3, i4):
                    continue
                l4 = [i1, i2, i3, i4]
                for i5 in range(i4 + 1, len(primes_list)):
                    if is_prime_pair_set2(l4, i5):
                        s = sum(primes_list[i] for i in [i1, i2, i3, i4, i5])
                        min_value = min(min_value, s)

print("Result: ", min_value)