from sympy import totient

# inefficient solution
#def gcd(a, b):
#    while b:
#        a, b = b, a % b
#    return a
#
#def phi(n):
#    count = 0
#    for i in range(1, n + 1):
#        if gcd(i, n) == 1:
#            count += 1
#    return count
#
#max_value1 = 0
#max_num1 = 0
#for n in range(2, 1_000_000):
#    div = n / phi(n)
#    if max_value1 < div:
#        #print("itt")
#        max_valueq = div
#        max_num1= n
#print("Solution1 : ", max_num1)

max_value2 = 0
max_num2 = 0
for n in range(2, 1_000_000):
    tot = totient(n)
    div = n / tot
    #print("Div: ", div)
    if max_value2 < div:
        #print("itt")
        max_value2 = div
        max_num2 = n

print("Solution2 : ", max_num2)

