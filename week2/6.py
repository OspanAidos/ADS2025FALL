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
    elif l2:
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


