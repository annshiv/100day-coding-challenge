# Queue Class 
class Queue: 
	def __init__(self): 
		self.items = [] 


	def isEmpty(self): 
		return self.items == [] 

	def add(self, item): 
		self.items.append(item) 

	def pop(self): 
		return self.items.pop(0) 

	def front(self): 
		return self.items[0] 

	def printQueue(self): 
		for i in self.items: 
			print(i, end =" ") 
		print("") 


# Recursive Function to reverse the queue 
def reverseQueue(q): 

	# Base case 
	if (q.isEmpty()): 
		return

	# Dequeue current item (from front) 
	data = q.front()
	q.pop()

	# Reverse remaining queue 
	reverseQueue(q) 

	# Enqueue current item (to rear) 
	q.add(data) 


# Driver Code 
q = Queue() 
q.add(56) 
q.add(27) 
q.add(30) 
q.add(45) 
q.add(85) 
q.add(92) 
q.add(58) 
q.add(80) 
q.add(90) 
q.add(100) 
reverseQueue(q) 
q.printQueue() 
