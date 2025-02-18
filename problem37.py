import math
filtered_primes = [2]

for n in range(3, 1000000, 2):
    is_prime = True
    square = math.sqrt(n)
    for p in filtered_primes:
        if p < square + 1:
            if n % p  == 0:
                is_prime = False
                break
        else:
            break
    if is_prime:
        #s = str(n)
        #if '4' not in s and '6' not in s and '9' not in s:
        filtered_primes.append(n)

filtered_prime_set = set()
for p in filtered_primes:
    filtered_prime_set.add(p)

def is_truncable_primes_first(p):
    if p < 10:
        if p in [2,3,5,7]:
            return True
        else:
            return False
    first_removed =int(str(p)[1:])
    return p in filtered_prime_set and is_truncable_primes_first(first_removed)

def is_truncable_primes_last(p):
    if p < 10:
        if p in [2,3,5,7]:
            return True
        else:
            return False
    last_removed = p // 10
    return p in filtered_prime_set and is_truncable_primes_last(last_removed)

collect = []
for p in filtered_primes:
    if is_truncable_primes_first(p) and is_truncable_primes_last(p):
        if p > 10:
            collect.append(p)
            print("primes: ", p)

print("sum: ", sum(collect))
