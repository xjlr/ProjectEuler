

f = open("problem22.txt", "r")

def strValue(str):
    sum = 0
    for s in str:
        sum = sum + ord(s) - 64
    return sum

line = []
for s in f:
    line = line + ([x for x in s.split("\",\"")])

line[0] = line[0].replace("\"", "")
line[-1] = line[-1].replace("\"", "")

line.sort()

print line.index('COLIN')
print strValue('COLIN')

totalScore = 0
for idx in range(0, len(line)):
    totalScore = totalScore + (idx + 1)*strValue(line[idx])

print "Total: ", totalScore


