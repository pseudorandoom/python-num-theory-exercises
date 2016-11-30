import random
import itertools


def encontrarMultiploResta(n, ns):
    perm = itertools.permutations(ns, r=2)
    for p in perm:
        if p[0] > p[1] and (p[0] - p[1]) % n == 0:
            return p

n = 0
while n < 2:
    try:
        n = int(input("ingrese un numero ≥ 2: "))
    except:
        print("la entrada no fue un numero")

a = set()
for _ in range(n + 1):
    a.add(random.randint(1, 1000))

print(encontrarMultiploResta(n, a))