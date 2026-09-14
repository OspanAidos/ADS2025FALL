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