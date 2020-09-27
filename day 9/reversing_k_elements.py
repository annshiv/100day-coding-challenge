from queue import Queue 

# Function to reverse the first K 
# elements of the Queue 
def reverseQueueFirstKElements(k, Queue): 
	if (Queue.empty() == True or
			k > Queue.qsize()): 
		return
	if (k <= 0): 
		return

	Stack = [] 

	# put the first K elements 
	# into a Stack 
	for i in range(k): 
		Stack.append(Queue.queue[0]) 
		Queue.get() 

	# Enqueue the contents of stack 
	# at the back of the queue 
	while (len(Stack) != 0 ): 
		Queue.put(Stack[-1]) 
		Stack.pop() 

	# Remove the remaining elements and 
	# enqueue them at the end of the Queue 
	for i in range(Queue.qsize() - k): 
		Queue.put(Queue.queue[0]) 
		Queue.get() 

# Utility Function to print the Queue 
def Print(Queue): 
	while (not Queue.empty()): 
		print(Queue.queue[0], end =" ") 
		Queue.get() 