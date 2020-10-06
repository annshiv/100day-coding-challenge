class Node:

    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key

def inorder(root):
    if root:
        inorder(root.left)

        print(root.val)

        inorder(root.right)

def postorder(root):
    if root:

        postorder(root.left)

        postorder(root.right)

        print(root.val)

def preorder(root):
    if root:

        print(root.val)

        postorder(root.left)

        postorder(root.right)

root = Node(1)

root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Preorder binary tree: ")
preorder(root)

print("inorder binary tree: ")
inorder(root)

print("Postorder binary tree: ")
postorder(root)