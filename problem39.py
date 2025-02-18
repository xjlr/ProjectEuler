def number_of_triples(p):
    num = 0
    for c in range(p//3, p//2):
        a = 1
        b = p - c - 1
        c2 = c**2
        while a <= b:
            a2b2 = a**2 + b**2
            if a2b2 == c2:
                num += 1
                #print("a: ", a)
                #print("b: ", b)
                #print("c: ", c)
                break
            if a2b2 < c2:
                break
            a += 1
            b -= 1
            #print("a: ", a)
            #print("b: ", b)
    return num

candidateP = -1
maxTriple = -1

for p in range(1, 1001):
    #print("p: ", p)
    #mapP = max(maxP, number_of_triples(p))
    numTriple = number_of_triples(p)
    if maxTriple < numTriple:
        maxTriple = numTriple
        candidateP = p

print("candidateP: ", candidateP)