class Node:
    def __init__ (self, data):
        self.data = data # This is the presend nodes data
        self.next = None # This is the next node

class LinkedList:
    def __init__(self):
        self.head = None # This is the present node.

    # Traversing through the Linked List
    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next

    # Adding node to start
    def push(self, new_data): 

        # Allocate the node and put in the data
        new_node = Node(new_data)

        # Make next of new node as head
        new_node.next = self.head

        # Move the head to put to the new node
        self.head = new_node

    # Adding node after another node
    def insertAfter(self, prev_node, new_data):

        # Check if the node is present
        if prev_node is None:
            print("Node should be present")
            return

        # Allocate the node and put in the data
        new_node = Node(new_data)

        # Make next of new Node as next of prev_node
        new_node.next = prev_node.next

        # Change next of prev Node as new_node
        prev_node.next = new_node

    def append(self, new_data):

        # Allocate the node and put in the data
        new_node = Node(new_data)

        # If the Linked List is empty, make the new_node as head
        if self.head is None:
            self.head = new_node
            return

        # Traverse till the end
        last = self.head
        while(last.next):
            last = last.next

        # Change Next of last node as new_node
        last.next = new_node
        pass

llist = LinkedList()

llist.head = Node(1)
second = Node(2)
third = Node(3)

llist.head.next = second
second.next = third

llist.printList()
print("--------------------")

# Pushing a node at the start
llist.push(0)

# Pushing a node after another node
llist.insertAfter(second, 5)

# Pushing a node after a node that is not in the Linked List
l2list = LinkedList()
llist.insertAfter(l2list.head,6)

# Pushing a node at the end
llist.append(4)

llist.printList()