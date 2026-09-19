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
    for val in values[1:]:
        current.next = Node(val)
        current = current.next
    return head
def den(head):
    current = head
    while current and current.next:
        current.next = current.next.next
        current = current.next
    return head
def pl(head):
    result = []
    current = head
    while current:
        result.append(str(current.val))
        current = current.next
    print(' '.join(result))
n = int(sys.stdin.readline())
values = list(map(int, sys.stdin.readline().split()))
head = bl(values)
head = den(head)
pl(head)