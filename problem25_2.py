

F1 = 1
F2 = 1

F3 = F1 + F2
count = 3
while len(str(F3)) < 1000:
    count = count + 1
    F1 = F2
    F2 = F3
    F3 = F1 + F2

print "count: ", count
