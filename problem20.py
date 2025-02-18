import math

N = math.factorial(100)

digits = []
while N:
    digits.append(N % 10)
    N = N / 10

print "Sum: ", sum(digits)
