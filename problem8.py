f = open('problem8.txt', 'r')
l = []

def splitNumber(string):
    return [(int)(char) for char in string]

def product(s):
    print s
    prod = 1
    for i in s:
        prod = prod * i

    return prod

for x in f:
    l = l + splitNumber(x.strip())

maxProd = 0
for i in range(0, len(l) - 13):
    prod = product(l[i:i+13])
    if maxProd < prod:
        maxProd = prod

print maxProd

