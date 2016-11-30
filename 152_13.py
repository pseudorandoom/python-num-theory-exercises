import math


def primo(n):
    for i in range(2, int(math.sqrt(n)+1)):
        if n % i == 0:
            return False
    return True

n = 0
while not 0 < n:
    try:
        n = int(input("ingrese un entero positivo: "))
    except:
        print("la entrada no fue un numero")

for i in range(n, 2 * n + 1):
    if primo(i):
        print(i)
        break

for i in range(2*n, n**2 + 1):
    if primo(i):
        print(i)
        break

