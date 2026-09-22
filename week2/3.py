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
    result = []
    current = head
    while current:
        result.append(str(current.val))
        current = current.next
    print("".join(result))
def cdb(head):
    if not head:
        return None
    current = head
    while current and current.next:
        if current.next.val == current.val:
            current.next = current.next.next
        else:
            current = current.next
    return head
def length(head):
    count = 0
    current = head
    while current:
        count += 1
        current = current.next
    return count
n = int(sys.stdin.readline()); s = []
for i in range(n):
    a = sys.stdin.readline()
    s.append(a)
head = bl(s)
head = cdb(head)
print(length(head))
pl(head)