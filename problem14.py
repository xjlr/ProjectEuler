
def countCollatz(num):
    count = 1
    while num != 1:
        count = count + 1
        if num % 2 == 0:
            num = num / 2
        else:
            num = 3 * num + 1

    return count

maxLength = 0
startingNumber = 0

for i in range(2, 1000000):
    length = countCollatz(i)
    if maxLength < length:
        maxLength = length
        startingNumber = i

print "#collatz: ", countCollatz(13)
print "#max length: ", maxLength
print "#starting number: ", startingNumber
