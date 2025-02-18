sum = 0
mod = 10000000000
for n in range(1, 1001):
    sum += n**n % mod
print(sum)