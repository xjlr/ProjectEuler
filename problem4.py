maxPalindrom = 0

def isPalindrom(product):
    productTemp = product

    candidate = 0

    while productTemp:
        candidate = candidate * 10 + productTemp % 10
        productTemp = productTemp / 10

    return product == candidate

print isPalindrom(9)
print isPalindrom(91)
print isPalindrom(919)
print isPalindrom(999)
print isPalindrom(9889)

for i in range(100, 1000):
    for j in range(i, 1000):
        product = i * j
        if maxPalindrom < product and isPalindrom(product):
            maxPalindrom = product

print maxPalindrom
