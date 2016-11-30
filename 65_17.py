def t(n):
    return int(n * (n + 1) / 2)


def palindromo(n):
    s = str(n)
    return s[::-1] == s

print([(x, t(x)) for x in range(9, 100) if palindromo(x) and palindromo(t(x))])