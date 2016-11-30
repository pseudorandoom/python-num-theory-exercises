import math


def primo(n):
    for i in range(2, int(math.sqrt(n)+1)):
        if n % i == 0:
            return False
    return True


def palindromo(n):
    s = str(n)
    return s[::-1] == s

print([x for x in range(2, 100) if primo(x) and palindromo(x)])