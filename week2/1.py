import sys
from collections import deque
def otg(guests):
    d = [0] * 26
    queue = deque()
    answer = []
    for guest in guests:
        index = ord(guest) - ord('a')
        d[index] += 1
        queue.append(guest)
        while queue:
            first = queue[0]
            first_index = ord(first) - ord('a')
            if d[first_index] == 1:
                break
            queue.popleft()
        if queue:
            answer.append(queue[0])
        else:
            answer.append('-1')
    return answer
n = int(sys.stdin.readline())
for i in range(n):
    t = int(sys.stdin.readline())
    s = deque(map(str, sys.stdin.readline().split()))
    print(*otg(s))

