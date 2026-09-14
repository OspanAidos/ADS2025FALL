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