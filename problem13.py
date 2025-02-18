import math
f = open('problem13.txt', 'r')

numbers = []
for x in f:
    numbers = numbers + ([(int)(n) for n in x.split()])

print "Numbers: ", numbers
print "Sum: ", sum(numbers)
