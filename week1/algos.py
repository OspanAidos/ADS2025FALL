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
# Алгоритм Евклида НОД
"""import sys
def gicidi(a, b):
    while b:
        a, b = b, a%b
    return a
n, m = map(int, sys.stdin.readline().split())
print(gicidi(n, m))
"""
# Modular exponential
"""
import sys
def expo(a,n,m, res = 1):
    a %= m
    res %= c
    while n:
        if n % 2 == 1:
            res *= a
            n-=1
        n //= 2
        a *= a
    return res
a, b, c = map(int, sys.stdin.readline().split())
print(expo(a, b, c))
"""
# Checking if C-Prime or not
"""import sys
from math import sqrt 
def cprime(n):
    if n < 2:
        return "NO"
    for i in range(2, int(sqrt(n))+1):
        if n%i == 0:
            return "NO"
    return "YES"
s = int(sys.stdin.readline())
print(cprime(s))
"""
# Checking D-Primes
"""
import sys
from math import sqrt

def is_prime(n):
    if n==2:
        return True
    if n%2 == 0:
        return False
    for i in range(3, int(sqrt(n)+1), 2):
        if n%i == 0:
            return False
    return True


def d_prime(n):
    if n == 1:
        return 2
    count = 1
    s = 3
    while count < n:
        if is_prime(s):
            count+=1
        if count == n:
            return s
        s+=2


a = int(sys.stdin.readline()) 
print(d_prime(a))
"""
# Prime factors
"""
import sys

def pr_f(n):
    i = 2
    a = []
    while i*i <= n:
        while n%i == 0:
            a.append(i)
            n//=i
        i += 1
    if n > 1:
        a.append(n)
    return a

b = int(sys.stdin.readline())
print(pr_f(b))
"""
# F-equal strings
"""
import sys
def fequal(n):
    a = []
    for i in n:
        if i != '#':
            a.append(i)
        elif a:
            a.pop()
    return a
a = sys.stdin.readline().strip()
b = sys.stdin.readline().strip()
if fequal(a) == fequal(b):
    print("Yes")
else:
    print("No")
"""
# G-balances sequence of letters
"""
import sys
def gb(s):
    s = list(s)
    a = []
    for i in s:
        if a and a[-1] == i:
            a.pop()
        else:
            a.append(i)
    return not a
n = sys.stdin.readline().strip()
print("YES") if gb(n) else print("NO")
"""
"""
# H-Nugman and Stack
import sys
def hns(n):
    a = []; b = []
    for i in n:
        while a and a[-1]>=i:
            a.pop()
        if not a:
            b.append('-1')
        else:
            b.append(str(a[-1]))
        a.append(i)
    return b
n = int(sys.stdin.readline())
s = map(int, sys.stdin.readline().split())
print(hns(s))
"""