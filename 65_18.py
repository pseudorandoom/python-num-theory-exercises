def t():
    n = 0
    while True:
        x = int(n * (n + 1) / 2)
        s = str(x)
        todos_iguales = s[0] * len(s)
        if x > 10 and s == todos_iguales:
            yield x
        n += 1

r = []
for i in t():
    r.append(i)
    if len(r) >= 3:
        break

print(r)