from queue import Queue 

def minIndex(q, sortedIndex): 
	min_index = -1
	min_val = 999999999999
	n = q.qsize() 
	for i in range(n): 
		curr = q.queue[0] 
		q.get()
		if (curr <= min_val and i <= sortedIndex): 
			min_index = i 
			min_val = curr 
		q.put(curr)
	return min_index 

# Moves given minimum element to 
# rear of queue 
def insertMinToRear(q, min_index): 
	min_val = None
	n = q.qsize() 
	for i in range(n): 
		curr = q.queue[0] 
		q.get() 
		if (i != min_index): 
			q.put(curr) 
		else: 
			min_val = curr 
	q.put(min_val) 

def sortQueue(q): 
	for i in range(1, q.qsize() + 1): 
		min_index = minIndex(q, q.qsize() - i) 
		insertMinToRear(q, min_index) 
