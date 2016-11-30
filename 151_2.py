import random


def encontrarSumaMultiploN(n, ns, rs):
    suma = sum(rs)
    if rs and suma % n == 0:
       return (suma, rs)
    else:
        for x in ns - rs:
            it = encontrarSumaMultiploN(n, ns, rs | {x})
            if it:
                return it

n = 0
while n < 2:
    try:
        n = int(input("ingrese un numero ≥ 2: "))
    except:
        print("la entrada no fue un numero")

a = set()
for _ in range(n):
    a.add(random.randint(1, 1000))

print('respuesta', "no encontrado" and encontrarSumaMultiploN(n, a, set()))