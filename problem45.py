def get_triangle(n):
    return n * (n + 1) // 2

def get_pentagonal(n):
    return n * (3*n - 1) // 2

def get_hexagonal(n):
    return n * (2*n - 1)

t = 285 + 1
p = 165
h = 143

while True:
    t_v = get_triangle(t)
    p_v = get_pentagonal(p)
    h_v = get_hexagonal(h)

    if t_v == p_v and p_v == h_v:
        print("t: %d, p: %d, h: %d", (t, p, h))
        print("value: %d", t_v)
        break
    
    min_v = min(t_v, p_v, h_v)
    if t_v == min_v:
        t += 1
    elif p_v == min_v:
        p += 1
    else:
        h += 1