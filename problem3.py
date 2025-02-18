import math

largestPrime = 1
num = 600851475143

for i in range(3, (int)(math.sqrt(600851475143)) + 1, 2):
    if num % i == 0:
        largestPrime = i
        num = num / i
        i = i - 1


print largestPrime
