import sys
from collections import deque
def irf(n):
    res = deque()
    for i in range(n, 0, -1):
        res.appendleft(i)
        res.rotate(i)
    return res
a = int(sys.stdin.readline())
s = deque()
for i in range(a):
    b = int(sys.stdin.readline())
    s.append(b)
for i in s:
    print(*irf(i))