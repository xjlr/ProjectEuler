import math
primes = [2]

def get_circular_numbers(n):
    l = [n]

    num_digits = int(math.log(n, 10)) + 1
    for xxx in range(1, num_digits):
        last = n % 10
        n //= 10
        n += last * 10**(num_digits - 1)
        l.append(n)
    return l

for n in range(3, 1000000, 2):
    is_prime = True
    square = math.sqrt(n)
    for p in primes:
        if p < square + 1:
            if n % p  == 0:
                is_prime = False
                break
        else:
            break
    if is_prime:
        primes.append(n)

#print("1300: ", get_circular_numbers(1300))
count = 0
#collect = set()
for p in primes:
    circ_num = get_circular_numbers(p)
    found = True
    for n in circ_num:
        if n not in primes:
            found = False
            break
    if found:
        #collect.add(p)
        count += 1

print(count)
#print(collect)
#plist = [x for x in primes]
#plist.sort()
#print(plist)
