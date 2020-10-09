class Node:

    def __init__(self,key):
        self.key = key
        self.right = self.left = None
    
def findlca(root,n1,n2):
    
    if root is None:
        return None
    
    if root.key == n1 or root.key == n2:
        return root
    
    left_lca = findlca(root.left,n1,n2)
    right_lca = findlca(root.right,n1,n2)

    if left_lca and right_lca:
        return root

    return left_lca if left_lca is not None else right_lca

root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(4) 
root.left.right = Node(5) 
root.right.left = Node(6) 
root.right.right = Node(7) 
print("LCA(4,5) = ", findlca(root, 4, 5).key)
print("LCA(4,6) = ", findlca(root, 4, 6).key) 
print("LCA(3,4) = ", findlca(root, 3, 4).key)
print("LCA(2,4) = ", findlca(root, 2, 4).key)