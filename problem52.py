from collections import Counter

def is_permuted_multiple(x):
    base_counter = Counter(str(x))
    # return all(Counter(str(i * x)) == base_counter for i in [6, 5, 4, 3, 2])
    return all(Counter(str(i * x)) == base_counter for i in [2, 3, 4, 5, 6])

n = 12
while True:
    # print("Try: ", n)
    if is_permuted_multiple(n):
        print("Result: ", n)
        break;
    n += 1

