# palos = ['treboles', 'diamantes', 'corazones', 'picas']
# valores = ['as', 'dos', 'tres', 'cuatro', 'cinco', 'seis', 'siete', 'ocho', 'nueve', 'diez', 'jota', 'reina', 'rey']
# cartas = [j + " de " + i for i in palos for j in valores]
# carta = -1
# while carta < 0 or carta > 51:
#     try:
#         carta = int(input('ingrese el numero de una carta entre 0 y 51: '))
#     except:
#         print("debe ingresar un numero")
# print("carta:", cartas[carta])

from math import factorial


def coeficiente_binomial(k, n):
    return int(factorial(n)/(factorial(k) * factorial(n-k)))

n = -1
while n < 0:
    try:
        n = int(input('ingrese un numero positivo: '))
    except:
        print("debe ingresar un numero")

p = [1]
for i in range(n):
    for j in range(i + 1):
        print(coeficiente_binomial(j,i), end=",")
    print()