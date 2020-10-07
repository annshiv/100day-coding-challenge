class Node:
    def __init__(self,data):
        self.val = data
        self.left = self.right = None
    
def binary_min(root): 
	if root is None: 
		return float('inf') 
	res = root.val 
	lres = binary_min(root.left) 
	rres = binary_min(root.right) 
	if lres < res: 
		res = lres 
	if rres < res: 
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

print("Minimum element is ",binary_min(root))