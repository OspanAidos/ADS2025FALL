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