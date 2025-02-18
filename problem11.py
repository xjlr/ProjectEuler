f = open('problem11.txt', 'r')

matrix = []
maxProduct = 0


def prodPosition(i, j):
    downProd = 0
    leftProd = 0
    diagProd1 = 0
    diagProd2 = 0
    try:
        downProd = matrix[i][j] * matrix[i][j + 1] * matrix[i][j + 2] * matrix[i][j + 3]
    except IndexError:
        downProd = 0

    try:
        leftProd = matrix[i][j] * matrix[i + 1][j] * matrix[i + 2][j] * matrix[i + 3][j]
    except IndexError:
        leftProd = 0

    try:
        diagProd1 = matrix[i][j] * matrix[i - 1][j + 1] * matrix[i - 2][j + 2] * matrix[i - 3][j + 3]
    except IndexError:
        diagProd1 = 0

    try:
        diagProd2 = matrix[i][j] * matrix[i + 1][j + 1] * matrix[i + 2][j + 2] * matrix[i + 3][j + 3]
    except IndexError:
        diagProd2 = 0

    return max(downProd, leftProd, diagProd1, diagProd2)

for x in f:
    matrix.append([(int)(n) for n in x.split()])

print matrix
for i in range(0, len(matrix[0])):
    for j in range(0, len(matrix[0])):
        prod = prodPosition(i, j)
        if maxProduct < prod:
            maxProduct = prod

print maxProduct
