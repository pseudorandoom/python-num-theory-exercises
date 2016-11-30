n = 0
while not 0 < n <= 20:
    try:
        n = int(input("ingrese un numero entre 0 y 20: "))
    except:
        print("la entrada no fue un numero")


def catalan(n):
    if n <= 1:
        return 1
    res = 0
    for i in range(n):
        res += catalan(i) * catalan(n - i - 1)
    return res

print(catalan(n))