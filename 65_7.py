def sumaDigitos(n):
    r = 0
    while n >= 1:
        r += (n % 10)**3
        n //= 10
    return r

print([x for x in range(100, 1000) if x == sumaDigitos(x)])