edge = range(3, 1002, 2)

sum = 1
sum2 = 1
for n in edge:
    sum = sum + 4*(n**2)
    sum = sum - 6*n
    sum = sum + 6

print "Sum: ", sum
