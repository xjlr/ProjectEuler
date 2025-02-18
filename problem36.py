def is_palindrom(n):
  m = n
  res = 0
  while n:
    res *= 10
    res += n % 10
    n //= 10

  return res == m

sum = 0
for n in range(1, 1000000):
    if is_palindrom(n):
        s = "{0:b}".format(n)
        if s == s[::-1]:
            sum += n

print(sum)
