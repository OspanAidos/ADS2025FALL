import sys
import math
def pow_f(a,b,c,res=1):
    res = 1%c
    while b>0:
        if b%2==1:
            res = a*res%c
        b = b//2
        a = a * a % c
    return res

n,m,p = map(int, sys.stdin.readline().split())
print(pow_f(n,m,p))