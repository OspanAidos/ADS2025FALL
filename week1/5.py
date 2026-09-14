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