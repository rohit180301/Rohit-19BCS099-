# Tree traversal
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
    def PostOrder(self, root):
        if root:
            self.PostOrder(root.left)
            self.PostOrder(root.right)
            print(root.val)
    def PreOrder(self, root):
        if root:
            print(root.val)
            self.PreOrder(root.left)
            self.PreOrder(root.right)
    def Inorder(self, root):
        if root:
            self.Inorder(root.left)
            print(root.val)
            self.Inorder(root.right)
# Main program
root = Node("A")
root.left = Node("B")
root.right = Node("C")
root.left.left = Node("D")
root.left.right = Node("E")
root.right.left = Node("F")
root.right.right = Node("G")
print("Preorder traversal of binary tree is")
root.PreOrder(root)
print("\nInorder traversal of binary tree is")
root.Inorder(root)
print("\nPostorder traversal of binary tree is")
root.PostOrder(root)
