import math


def es_primo(n):
    for i in range(3, int(math.sqrt(n)+1), 2):
        if n % i == 0:
            return False

    return True

primes = [2]
even = []


def sacar_suma_primos(n):
    return n, [(x, y) for x in primes for y in primes if x + y == n]


for i in range(3, 100):
    if i %2 == 0:
        even.append(sacar_suma_primos(i))
    elif es_primo(i):
        primes.append(i)

for e in even:
    print(e)
