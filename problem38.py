def are_digits_distinct_and_no_zero(number):
    digits = set()
    for digit in str(number):
        if digit == '0' or digit in digits:
            return False
        digits.add(digit)
    return True

def concatenate(numbers):
    n_str = ""
    for n in numbers:
        n_str = n_str + str(n)
    return int(n_str)

max = -1
exp = 1
for n in range(5, 1, -1):
    print(n)
    k = 1
    exp = exp * 10
    #numbers_list = [i for i in range(1, n + 1)]
    while k < exp:
        numbers_list = [i*k for i in range(1, n + 1)]
        cand_max = concatenate(numbers_list)
        if (cand_max > max and are_digits_distinct_and_no_zero(cand_max)):
            max = cand_max
        k = k + 1

print(max)    
