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