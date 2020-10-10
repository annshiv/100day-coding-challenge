class Node: 
	
	# Constructor to create a new node 
	def __init__(self, data): 
		self.data = data 
		self.right = None
		self.left = None

def flipBinaryTree(root): 
	
	# Base Cases 
	if root is None: 
		return root 
	
	if root.left is None and root.right is None: 
		return root 

	# Recursively call the same method 
	flippedRoot = flipBinaryTree(root.left) 

	# Rearranging main root Node after returning 
	# from recursive call 
	root.left.left = root.right 
	root.left.right = root 
	root.left = root.right = None

	return flippedRoot 

# Iterative method to do the level order traversal 
# line by line 
def printLevelOrder(root): 
	
	# Base Case 
	if root is None: 
		return
	
	# Create an empty queue for level order traversal 
	from Queue import Queue 
	q = Queue() 
	
	# Enqueue root and initialize height 
	q.put(root) 
	
	while(True): 

		# nodeCount (queue size) indicates number 
		# of nodes at current level 
		nodeCount = q.qsize() 
		if nodeCount == 0: 
			break

		# Dequeue all nodes of current level and 
		# Enqueue all nodes of next level 
		while nodeCount > 0: 
			node = q.get() 
			print(node.data) 
			if node.left is not None: 
				q.put(node.left) 
			if node.right is not None: 
				q.put(node.right) 
			nodeCount -= 1



# Driver code 
root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.right.left = Node(4) 
root.right.right = Node(5) 

print("Level order traversal of given tree")
printLevelOrder(root) 

root = flipBinaryTree(root) 

print("\nLevel order traversal of the flipped tree")
printLevelOrder(root) 