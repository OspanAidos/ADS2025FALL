import math
import sys
def main(s):
    stack = []
    for i in s:
        if i != '#':
            stack.append(i)
        elif stack:
            stack.pop()
    return stack
str1 = sys.stdin.readline().strip()
str2 = sys.stdin.readline().strip()
if main(str1) == main(str2):
    print('Yes')
else:
    print('No')

            

    