"""
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
for _ in range(n):
    t = int(sys.stdin.readline())
    s = deque(map(str, sys.stdin.readline().split()))
    print(*otg(s))
"""
"""
import sys
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
def bl(values):
    if not values:
        return None
    head = Node(values[0])
    current = head
    for value in values[1:]:
        current.next = Node(value)
        current = current.next
    return head
def pl(head):
    current = head
    res = []
    while current:
        res.append(str(current.val))
        current = current.next
    print(' '.join(res))
def den(head):
    current = head
    while current and current.next:
        current.next = current.next.next
        current = current.next
    return head
n = int(sys.stdin.readline())
values = list(map(int, sys.stdin.readline().split()))
head = bl(values)
head = den(head)
pl(head)
"""
"""
import sys
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
def bl(values):
    if not values:
        return None
    head = Node(values[0])
    current = head
    for value in values[1:]:
        current.next = Node(value)
        current = current.next
    return head
def pl(head):
    current = head
    res = []
    while current:
        res.append(str(current.val))
        current = current.next
    print(' '.join(res))
def rev(head):
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev
n = int(sys.stdin.readline())
s = list(map(int, sys.stdin.readline().split()))
head = bl(s)
head = rev(head)
pl(head)
"""
"""
import sys
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
def bl(values):
    if not values:
        return None
    head = Node(values[0])
    current = head
    for value in values[1:]:
        current.next = Node(value)
        current = current.next
    return head
def pl(head):
    res = []
    current = head
    while current:
        res.append(str(current.val))
        current = current.next
    print(' '.join(res))
def length(head):
    count = 0
    current = head
    while current:
        count += 1
        current = current.next
    return count
def middle(head):
    if not head or not head.next:
        return None
    current  = head; num = length(head)
    for _ in range(num//2-1):
        current = current.next
    current.next = current.next.next
    return head
n = int(sys.stdin.readline())
s = list(map(int, sys.stdin.readline().split()))
head = bl(s)
head = middle(head)
pl(head)
"""
"""
import sys
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
def bl(values):
    if not values:
        return None
    head = Node(values[0])
    current = head
    for value in values[1:]:
        current.next = Node(value)
        current = current.next
    return head
def pl(head):
    s = []
    current = head
    while current:
        s.append(str(current.val))
        current = current.next
    print(' '.join(s))
def ml(l1, l2):
    dummy = Node(0)
    tail = dummy
    while l1 and l2:
        if l1.val <= l2.val:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next
    if l1:
        tail.next = l1
    if l2:
        tail.next = l2
    return dummy.next
line1 = list(map(int, sys.stdin.readline().split()))
line2 = list(map(int, sys.stdin.readline().split()))
n = line1[0]
vals1 = line1[1:n+1] if n>0 else []
m = line2[0]
vals2 = line2[1:m+1] if m>0 else []
l1 = bl(vals1)
l2 = bl(vals2)
merged_list = ml(l1, l2)
pl(merged_list)
"""
"""
import sys
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
def bl(values):
    if not values:
        return None
    head = Node(values[0])
    current = head
    for value in values[1:]:
        current.next = Node(value)
        current = current.next
    return head
def pl(head):
    res = []
    current = head
    while current:
        res.append(str(current.val))
        current = current.next
    print(' '.join(res))
def rot(head, k):
    if not head or not head.next or k == 0:
        return head
    current = head
    for _ in range(k-1):
        current = current.next
    kth_node = current
    new_head = kth_node.next
    if not new_head:
        return head
    kth_node.next = None
    tail = new_head
    while tail.next:
        tail = tail.next
    tail.next = head
    return new_head
a, b = map(int, sys.stdin.readline().split())
words = list(map(str, sys.stdin.readline().split()))
head = bl(words)
head = rot(head, b)
pl(head)
"""