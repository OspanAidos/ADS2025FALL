import sys
def age_d(n):
    a=[]
    for i in n:
        if a[-1] < i:
            a.append(a[-1])
        else:
            a.append(-1)
    return a.pop()
n=int(sys.stdin.readline())
g=[]
g=list(map(int, sys.stdin.readline().split()))
print(age_d(g))