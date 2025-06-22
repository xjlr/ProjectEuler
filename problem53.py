import math

def first_greater_than(n, threshold=1_000_000):
    left = 1
    right = n // 2
    
    while left < right:
        mid = (left + right) // 2
        if math.comb(n, mid) > threshold:
            right = mid
        else:
            left = mid + 1
    
    if math.comb(n, left) > threshold:
        return left
    else:
        return -1

def get_number_which_greater_than_threshold(n, threshold=1_000_000):
    num = first_greater_than(n, threshold)
    if num == -1:
        return 0
    else:
        return n + 1 - 2 * num

sum = 0
for i in range(1, 101):
    sum += get_number_which_greater_than_threshold(i)

print("Result: ", sum)