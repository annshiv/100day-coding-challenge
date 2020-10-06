class Node:

    def __init__(self,data):
        self.val = data
        self.right = None
        self.left = None
    
def printlevelorder(root):
    
    if root is None:
        return 
    
    q = []
    q.append(root)

    while q:
        count = len(q)

        while count > 0:
            temp = q.pop(0)

            print(temp.val, end=" ")

            if temp.left:
                q.append(temp.left)
            if temp.right:
                q.append(temp.right)
            count -= 1
        print(' ')

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(6)

printlevelorder(root)