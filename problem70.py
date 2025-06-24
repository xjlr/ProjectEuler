from collections import Counter
from sympy import totient

min_div = float('inf')
min_n = -1

for n in range(2, 10_000_000):
    tot = totient(n)
    if Counter(str(n)) == Counter(str(tot)):
        div = n / tot
        if div < min_div:
            min_div = div
            min_n = n

print("Result: ", min_n)