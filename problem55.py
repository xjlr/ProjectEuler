def is_palindrome(n):
    return str(n) == str(n)[::-1]

def reverse_number(n):
    reversed_str = str(n)[::-1]
    return int(reversed_str)
   
def is_lychrel_number(n):
    current = n
    for i in range(50):
        current = current + reverse_number(current)
        if is_palindrome(current):
            return False  # Not a Lychrel number
    return True  # Likely a Lychrel number

lychrel_cnt = 0

for n in range(1, 10000):
    if is_lychrel_number(n):
        lychrel_cnt += 1

print("Result: ", lychrel_cnt)