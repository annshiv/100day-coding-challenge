class Node:
    def __init__(self,data):
        self.val = data
        self.left = self.right = None
    
def binary_max(root):

    if (root == None):
        return float('-inf')

    res = root.val
    lres = binary_max(root.left)
    rres = binary_max(root.right)

    if(lres > res):
        res = lres
    if(rres > res):
        res = rres
    return res

root = Node(2)
root.left = Node(7)
root.right = Node(5)
root.left.right = Node(6)
root.left.left = Node(1)
root.left.right.left = Node(11)
root.left.right.right = Node(3)
root.right.right = Node(9)

print("Maximum element is ",binary_max(root))