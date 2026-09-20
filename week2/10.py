import sys
class Node:
    def __init__(self, val):
        self.val = val
        self.next = next
def insert(head, x, p):
    new_node = Node(x)
    if p == 0:
        new_node.next = head
        return new_node
    current = head
    for _ in range(p-1):
        current = current.next 
    new_node.next = current.next
    current.next = new_node
    return head
def remove(head, p):
    if head is None:
        return None
    if p == 0:
        return head.next
    current = head
    for _ in range(p-1):
        current = current.next
    if current.next:
        current.next = current.next.next
    return head
def pl(head):
    if head is None:
        print(-1)
        return 
    res = []
    current = head
    while current:
        res.append(str(current.val))
        current = current.next
    print(' '.join(res))
def replace(head, p1, p2):
    current = head
    for _ in range(p1):
        current = current.next
    val = current.val
    head = remove(head, p1)
    head = insert(head, val, p2)
    return head
def reverse(head):
    prev = None
    current = head
    while current:
        next = current.next
        current.next = prev
        prev = current
        current = next
    return prev
def length(head):
    count = 0
    current = head
    while current:
        count += 1
        current = current.next
    return count
def cyclic_left(head, x):
    leng = length(head)
    if leng <= 1:
        return head
    x %= leng
    if x == 0:
        return head
    current = head
    for _ in range(x-1):
        current = current.next
    new_head = current.next
    current.next = None
    tail = new_head
    while tail.next:
        tail = tail.next
    tail.next = tail.next = head
    return new_head
def cyclic_right(head, x):
    leng = length(head)
    if leng <= 1:
        return head
    x %= leng
    if x == 0:
        return head
    return cyclic_left(head, leng - x)
tokens = sys.stdin.read().split()
it = iter(tokens)
head = None
for token in it:
    cmd = int(token)
    if cmd == 0:
        break
    elif cmd == 1:
        x, p = int(next(it)), int(next(it))
        head = insert(head, x, p)
    elif cmd == 2:
        p = int(next(it))
        head = remove(head, p)
    elif cmd == 3:
        pl(head)
    elif cmd == 4:
        p1, p2 = int(next(it)), int(next(it))
        head = replace(head, p1, p2)
    elif cmd == 5:
        head = reverse(head)
    elif cmd == 6:
        x = int(next(it))
        head = cyclic_left(head, x)
    elif cmd == 7:
        x = int(next(it))
        head = cyclic_right(head, x)
