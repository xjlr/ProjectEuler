l = sorted(str(123456789))

def isPandigital(s):
    return sorted(s) == l

nums = set()
for i in range(1, 999):
    for j in range(10, 9999):
        s = str(i) + str(j)
        p = i * j
        s += str(p)
        if isPandigital(s):
            #print(p, "==", i, " * ", j)
            nums.add(p)

print("sum: ", sum(nums))
