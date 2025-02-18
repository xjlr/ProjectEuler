def numberOfWaysToMakeChange(n, denoms):
    denoms.sort()
    a = [0] * (n + 1)
    a[0] = 1
    for d in denoms:
        for idx in range(d, n + 1):
            a[idx] += a[idx - d]      
    return a[n]
