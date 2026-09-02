import sys
import math
input = sys.stdin.readline
s = True
a=int(input())
if a <= 1:
    print('NO')
else:
    s = True
    for i in range(2,int(math.sqrt(a)) + 1):
        if a%i==0:
            s = False
            break
    if s:
        print('YES')
    else:
        print('NO')