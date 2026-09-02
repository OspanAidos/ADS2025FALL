import sys
import math
def is_prime(n):
    if n<=1:
        return False
    else:
        for i in range(2,int(math.sqrt(n))+1):
            if n%i==0:
                return False
        return True
input = sys.stdin.readline
n = int(input())
i = 0; t = 0; s = 2
while i != n:
    if is_prime(s):
        t=s
        i+=1
    if i == n:
        break
    s+=1
print(s)