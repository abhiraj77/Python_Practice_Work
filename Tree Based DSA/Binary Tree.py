class Node:
    def __init__ (self, data):
        self.left = None
        self.righ = None
        self.data = data

    def PrintTree(self):
        print(self.data)

root = Node(10)
root.PrintTree()