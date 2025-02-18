import math

found = False
abc = 0

for a in range(1,500):
    if found:
        break
    for b in range(a+1,500):
        c = 1000 - a - b
        if a**2 + b**2 == c**2:
            abc = a*b*c
            found = True
            break

print abc
