# Решето Эратосфена
"""
import sys
def erat(n):
    if n<2:
        return []
    a = [True] * (n+1)
    a[0] = a[1] = False
    for i in range(2, int(n**0.5+1)):
        if a[i]:
            size = len(range(i*i, n+1, i))
            a[i*i : n+1 : i] = [False] * size 
    return [i for i, is_prime in enumerate(a) if is_prime]
b = int(sys.stdin.readline())
print(*erat(b))
"""
# НОД
"""import sys
def gicidi(a, b):
    while b:
        a, b = b, a%b
    return a
n, m = map(int, sys.stdin.readline().split())
print(gicidi(n, m))
"""