# A binary tree node 
class Node: 

	# Constructor to create a new node 
	def __init__(self, data): 
		self.data = data 
		self.left = None
		self.right = None


# Recursive function pritn left view of a binary tree 
def leftViewUtil(root, level, max_level): 
	
	# Base Case 
	if root is None: 
		return

	if (max_level[0] < level): 
		print("% d\t" %(root.data))
		max_level[0] = level 

	leftViewUtil(root.left, level + 1, max_level) 
	leftViewUtil(root.right, level + 1, max_level)

def leftView(root): 
	max_level = [0] 
	leftViewUtil(root, 1, max_level) 
 
root = Node(12) 
root.left = Node(10) 
root.right = Node(20) 
root.right.left = Node(25) 
root.right.right = Node(40) 

leftView(root) 