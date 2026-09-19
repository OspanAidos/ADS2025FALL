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
def maxs(head):
    if not head:
        return 0
    max_so_far = head.val
    current_max = head.val
    current = head.next
    while current:
        current_max = max(current.val, current.val + current_max)
        max_so_far = max(max_so_far, current_max)
        current = current.next
    return max_so_far
n = int(sys.stdin.readline())
days = list(map(int, sys.stdin.readline().split()))
head = bl(days)
print(maxs(head))