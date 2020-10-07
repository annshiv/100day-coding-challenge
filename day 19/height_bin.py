class Node:

    def __init__(self,data):
        self.val = data
        self.left = self.right = None

def height(root):

    if root is  None:
        return 0 

    else:

        lhigh = height(root.left)
        rhigh = height(root.right)

        if (lhigh > rhigh):
            return lhigh + 1
        else:
            return rhigh + 1

root = Node(1)
root.right = Node(3)
root.left = Node(2)
root.left.left = Node(4)
root.left.right = Node(5)

print("Maximum height of tree ",height(root))