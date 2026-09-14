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
'''
ages = [2,1,5,8,3]; stack = []; result = []
age = 2; stack = [2]; result = [-1]
age = 1; stack = [1]; result = [-1, -1]
age = 5; stack = [1, 5]; result = [-1, -1, 1]
age = 8; stack = [1, 5, 8]; result = [-1, -1, 1, 5]
age = 3; stack = [1]; result = [-1, -1, 1, 5, 1]
'''