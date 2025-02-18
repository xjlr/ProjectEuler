import math

def getNum(i, j):
  return i * 10 + j

for i in range(1, 10):
  for j in range(1, 10):
    for k in range(1, 10):
      m = i / j
      m1 = getNum(i, k) / getNum(j, k)
      m2 = getNum(i, k) / getNum(k, j)
      m3 = getNum(k, i) / getNum(j, k)
      m4 = getNum(k, i) / getNum(k, j)
      if math.isclose(m, m1):
        print("1. ", i, j, k)

      if math.isclose(m, m2):
        print("2. ", i, j, k)

      if math.isclose(m, m3):
        print("3. ", i, j, k)

      if math.isclose(m, m4):
        print("4. ", i, j, k)
