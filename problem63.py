n = 1
cnt = 0
while True:
    k = 1
    found = False

    while len(str(k**n)) <= n:
        if len(str(k**n)) == n:
            cnt += 1
            found = True
        k += 1
    
    if not found:
        break
    n += 1

print("Result: ", cnt)