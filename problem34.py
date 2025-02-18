import math

fact = [math.factorial(x) for x in range(0, 10)]

def fact_sum(n_digits):
    sum = 0
    for d in n_digits:
        sum += fact[d]
    return sum

super_sum = 0
for n in range(10, 100000):
    n_digits = [int(x) for x in str(n)]
    sum = fact_sum(n_digits)
    if n == sum:
        print("sub res:", n)
        super_sum += n

print(super_sum )
