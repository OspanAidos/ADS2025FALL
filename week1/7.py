import sys
def age_d(ages):
    stack = []; result = []
    for age in ages:
        while stack and stack[-1] >= age:
            stack.pop()
        if not stack:
            result.append("-1")
        else:
            result.append(str(stack[-1]))
        stack.append(age)
    return result
n=int(sys.stdin.readline())
g=[]
g=list(map(int, sys.stdin.readline().split()))
print(*age_d(g))
'''
ages = [2,1,5,8,3]; stack = []; result = []
age = 2; stack = [2]; result = [-1]
age = 1; stack = [1]; result = [-1, -1]
age = 5; stack = [1, 5]; result = [-1, -1, 1]
age = 8; stack = [1, 5, 8]; result = [-1, -1, 1, 5]
age = 3; stack = [1]; result = [-1, -1, 1, 5, 1]
'''