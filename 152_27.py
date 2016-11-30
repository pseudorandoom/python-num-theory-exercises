import math


def f(n):
    return 1 - 1 / n ** 2


def primo(n):
    for i in range(2, int(math.sqrt(n)+1)):
        if n % i == 0:
            return False
    return True

p = 1
for i in [x for x in range(2, 1000) if primo(x)]:
    p *= f(i)

print(p)
