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
