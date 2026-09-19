import sys
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = Node()
    def append(self, data):
        new_node = Node(data)
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = new_node
    def display(self):
        elems = []
        cur = self.head
        while cur.next:
            cur = cur.next
            elems.append(cur.data)
        print(elems)
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head.next
        self.head.next = new_node

my_list = LinkedList()
my_list.append(1)
my_list.display()




