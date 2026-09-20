import sys
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None
def add_front(head, tail, title):
    new_node = Node(title)
    if not head:
        head = new_node
        tail = new_node
    else:
        new_node.next = head
        head.prev = new_node
        head = new_node
    print('ok')
    return head, tail
def add_back(head, tail, title):
    new_node = Node(title)
    if not tail:
        head = new_node
        tail = new_node
    else:
        new_node.prev = tail
        tail.next = new_node
        tail = new_node
    print('ok')
    return head, tail
def erase_front(head, tail):
    if not head:
        print('error')
        return head, tail
    val = head.val
    if head == tail:
        head = None
        tail = None
    else:
        head = head.next 
        head.prev = None
    print(val)
    return head, tail
def erase_back(head, tail):
    if not tail:
        print('error')
        return head, tail
    val = tail.val
    if head == tail:
        head = None
        tail = None
    else:
        tail = tail.prev
        tail.next = None
    print(val)
    return head, tail
def front(head):
    if not head:
        print('error')
    else:
        print(head.val)
def back(tail):
    if not tail:
        print('error')
    else:
        print(tail.val)
def clear():
    print('ok')
    return None, None
head = None
tail = None
line = list(map(str, sys.stdin.readline().split()))
while line and line[0] != 'exit':
    command = line[0]
    if command == 'add_front':
        head, tail = add_front(head, tail, line[1])
    elif command == 'add_back':
        head, tail = add_back(head, tail, line[1])
    elif command == 'erase_front':
        head, tail = erase_front(head, tail)
    elif command == 'erase_back':
        head, tail = erase_back(head, tail)
    elif command == 'front':
        front(head)
    elif command == 'back':
        back(tail)
    elif command == 'clear':
        head, tail = clear()
    line = list(map(str, sys.stdin.readline().split()))
print('goodbye')