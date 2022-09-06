class Node:
    def __init__ (self, data):
        self.data = data # This is the presend nodes data
        self.next = None # This is the next node

class LinkedList:
    def __init__(self):
        self.head = None # This is the present node.

    def PrintList(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next

    def push(self, val):
        
        pass

llist = LinkedList()

llist.head = Node(1)
second = Node(2)
third = Node(3)

llist.head.next = second
second.next = third
llist.PrintList()