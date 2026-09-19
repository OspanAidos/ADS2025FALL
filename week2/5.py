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
    current = head; num = length(head)
    for _ in range(num//2 - 1):
        current = current.next
    current.next = current.next.next
    return head
n = int(sys.stdin.readline())
s = list(map(int, sys.stdin.readline().split()))
head = bl(s)
head = middle(head)
pl(head)