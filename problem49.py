from sympy import isprime

def has_distinct_digits(n):
    return len(set(str(n))) == len(str(n))

#has_distinct_digits(n) and
prime_4_digits = [n for n in range(1000,10000) if isprime(n)]

#print(prime_4_digits)

for i in range(len(prime_4_digits)):
    p1 = prime_4_digits[i]
    for j in range(i + 1, len(prime_4_digits)):
        p2 = prime_4_digits[j]
        diff = p2 - p1
        p3 = p2 + diff
        if p3 in prime_4_digits:
            v1 = set(str(p1)) == set(str(p2))
            v2 = set(str(p2)) == set(str(p3))
            if v1 and v2:
                print("%d %d %d" % (p1, p2, p3))

#print(prime_4_digits)


