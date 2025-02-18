
d = {}

ar = br = range(2, 101)

for a in ar:
    for b in br:
        d[a**b] = True

print "Size: ", len(d)

