from sympy import factorint

n = 2

while True:
    if len(factorint(n)) == 4:
        if len(factorint(n+1)) == 4:
            if len(factorint(n+2)) == 4:
                if len(factorint(n+3)) == 4:
                    print(n)
                    break
                else:
                    n += 4
            else:
                n +=3
        else:
            n += 2
    else:
        n += 1
