def sum_digits(n):
    #return sum(int(d) for d in str(abs(n)))
    return sum(int(d) for d in str(n))

max_digit_sum = 0
for a in range(1, 100):
    for b in range(1, 100):
        sd = sum_digits(a**b)
        max_digit_sum = max(max_digit_sum, sd)


print("Result: ", max_digit_sum)
