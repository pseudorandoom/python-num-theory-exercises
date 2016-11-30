import math


def e(n):
    return n ** 2 - n + 41

def primo(n):
    for i in range(2, int(math.sqrt(n)+1)):
        if n % i == 0:
            return 'compuesto'
    return 'primo'

for i in [(e(x), primo(e(x))) for x in range(2, 42)]:
    print(i)