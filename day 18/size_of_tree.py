class Node:

    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    
def sizeofNode(root):
    
    if root is None:
        return 0
    else:
        return(sizeofNode(root.left) + 1 + (sizeofNode(root.right)))

root = Node(1)
root.left = Node(2) 
root.right = Node(3) 
root.left.left  = Node(4) 
root.left.right = Node(5)

print("Size of the tree is %d" %(sizeofNode(root)))

