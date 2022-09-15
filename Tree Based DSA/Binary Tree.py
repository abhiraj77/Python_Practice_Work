class Node:
    def __init__ (self, data):
        self.left = None
        self.right = None
        self.data = data

    # Print the Tree
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data)
        if self.right:
            self.right.PrintTree()

    # Insert Node
    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left:
                    self.left.insert(data)
                else:
                    self.left = Node(data)
            elif data > self.data:
                if self.right:
                    self.right.insert(data)
                else:
                    self.right = Node(data)
        else:
            self.data = data
    
    # Inorder Traversal 
    # Left->Root->Right
    def Inorder(self, root):
        result = []
        if root:
            result = self.Inorder(root.left)
            result.append(root.data)
            result = result + self.Inorder(root.right)
            print(result)
        return result

    # Preorder Traversal
    # Root->Left->Right
    def Preorder(self,root):
        result = []
        if root:
            result.append(root.data)
            result = result + self.Preorder(root.left)
            result = result + self.Preorder(root.right)
        return result
    
    # Postorder Traversal
    # Left->Right->Root
    def Postorder(self,root):
        result = []
        if root:
            result = self.Postorder(root.left)
            result = result + self.Postorder(root.right)
            result.append(root.data)
        return result

root = Node(27)
root.insert(14)
root.insert(35)
root.insert(10)
root.insert(19)
root.insert(31)
root.insert(42)
print(f"Inorder = {root.Inorder(root)}")
print(f"Preorder = {root.Preorder(root)}")
print(f"Postorder = {root.Postorder(root)}")