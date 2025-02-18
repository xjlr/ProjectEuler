f0 = 1
f1 = 2

sum = 2

f2 = 3

while f2 <= 4000000:
    f0 = f1
    f1 = f2
    f2 = f0 + f1
    if f2 % 2 == 0:
        sum = sum + f2

print sum
