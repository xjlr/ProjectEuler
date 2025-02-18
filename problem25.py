import math

squareFive = math.sqrt(5)

def fib(n):
    return ((1.0/squareFive) * (math.pow((1+squareFive)/2, n)) - (1.0/squareFive) * (math.pow((1-squareFive)/2, n)))

def length(n):
    return len(str(n))
print fib(5)
print fib(1)
print fib(12)


low = 1
high = 2
while length(fib(low)) > 1000 or 1000 > length(fib(high)):
    print "###low: ", low
    low = 2*low
    high = 2*high

print "low: ", low
print "high: ", high

