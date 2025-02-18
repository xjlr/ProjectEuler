from sympy import isprime

primes = [p for p in range(1, 10000) if isprime(p)]

def k_window_max(k):
    l = len(primes)
    assert(k <= l)

    s = sum(primes[0:k])
    for i in range(0, l - k):
        if isprime(s):
            if s >= 1000000:
                return(False, 0, 0)            
            return (True, s, primes[i])
        s = s - primes[i] + primes[i + k]
        # print(s)
    return(False, 0, 0)

# print(primes)

for i in range(len(primes), 1, -1):
    # print(i)
    result = k_window_max(i)
    if result[0]:
        print(result)
        break