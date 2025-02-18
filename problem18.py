f = open('problem18.txt', 'r')

pyramid = []
for x in f:
    pyramid.append([(int)(n) for n in x.split()])


print pyramid

bestPath = [pyramid[0]]

for row in range(1,len(pyramid)):
    tempBestRoute = []
    for col in range(0, len(pyramid[row])):
        prevValueLeft = 0
        prevValueRight = 0

        try:
            prevValueLeft = bestPath[-1][col - 1]
        except IndexError:
            prevValueLeft = 0

        try:
            prevValueRight = bestPath[-1][col]
        except IndexError:
            prevValueRight = 0

        value = pyramid[row][col] + max(prevValueLeft, prevValueRight)
        tempBestRoute.append(value)

    bestPath.append(tempBestRoute)


print bestPath
print "------------------"
print "Max route: ", max(bestPath[-1])
