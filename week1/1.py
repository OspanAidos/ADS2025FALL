import sys
import math
def gcd_f(a,b):
    while b:
        a, b = b, a%b
    return a
n,m = map(int, sys.stdin.readline().split())
print(gcd_f(n,m))
