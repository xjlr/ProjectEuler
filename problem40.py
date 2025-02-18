def create_champernowne(max_length):
    num = 0
    n_str = ''
    while len(n_str) < max_length + 1:
        n_str = n_str + str(num)
        num += 1
    return n_str

n_str = create_champernowne(1000000)
res = int(n_str[1]) * int(n_str[10]) * int(n_str[100]) * int(n_str[1000]) * int(n_str[10000]) * int(n_str[100000]) * int(n_str[1000000])
print(res)