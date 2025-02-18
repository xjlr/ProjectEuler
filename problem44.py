def get_pentagonal_number(n):
    return n*(3*n - 1)//2

pent_nums = set()
for j in range(1, 100001):
    pent_nums.add(get_pentagonal_number(j))

i = 1
found = False

while not found and i < 100000:
    i += 1
    #print(i)
    i_pent = get_pentagonal_number(i)

    j = i - 1
    while j > 0:
        j_pent = get_pentagonal_number(j)
        if ((i_pent + j_pent) in pent_nums) and (abs(i_pent - j_pent) in pent_nums):
            #found = True
            print("i: %d j: %d, diff: %d" % (i, j, i_pent - j_pent))
        #if found:
        #    break
        j -= 1
