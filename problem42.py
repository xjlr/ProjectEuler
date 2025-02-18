def word_value(word):
    return sum(ord(c) - 64 for c in word)

with open('problem42.txt', 'r') as file:
    content = file.read()
    words = [word.strip('"') for word in content.split(',')]

triangle_numbers = [n*(n+1)//2 for n in range(1, 31)]

w_values = [word_value(w) for w in words if word_value(w) in triangle_numbers]

print(len(w_values))

