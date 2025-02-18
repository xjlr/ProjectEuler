import itertools

def get_3digits_number_from_position(perm, n):
    return perm[n - 1] * 100 + perm[n] * 10 + perm[n + 1]

def is_valid_permutation(perm):
    if perm[0] == 0:
        return False
    if perm[3] % 2 != 0:
        return False
    if (perm[2] + perm[3] + perm[4]) % 3 != 0:
        return False
    if perm[5] != 5:
        return False
    if get_3digits_number_from_position(perm, 5) % 7 != 0:
        return False
    if get_3digits_number_from_position(perm, 6) % 11 != 0:
        return False
    if get_3digits_number_from_position(perm, 7) % 13 != 0:
        return False
    if get_3digits_number_from_position(perm, 8) % 17 != 0:
        return False
    return True


perms = itertools.permutations(range(0, 10))

filtered_perms = (perm for perm in perms if is_valid_permutation(perm))

result = 0
for perm in filtered_perms:
    number = int(''.join(map(str, perm)))
    result += number
    print(number)

print(result)


#three_digit_numbers = [int(f"{perm[1]}{perm[2]}{perm[3]}") for perm in filtered_perms]

#for number in three_digit_numbers:
#    print(number)


