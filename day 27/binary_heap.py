from heapq import heappush, heappop, heapify 

class MinHeap: 

	def __init__(self): 
		self.heap = [] 

	def parent(self, i): 
		return (i-1)/2

	def insertKey(self, k): 
		heappush(self.heap, k)		 

	def decreaseKey(self, i, new_val): 
		self.heap[i] = new_val 
		while(i != 0 and self.heap[self.parent(i)] > self.heap[i]): 
			self.heap[i] , self.heap[self.parent(i)] = ( 
			self.heap[self.parent(i)], self.heap[i]) 

	def extractMin(self): 
		return heappop(self.heap) 

	def deleteKey(self, i): 
		self.decreaseKey(i, float("-inf")) 
		self.extractMin() 

	def getMin(self): 
		return self.heap[0] 

heapObj = MinHeap() 
heapObj.insertKey(3) 
heapObj.insertKey(2) 
heapObj.deleteKey(1) 
heapObj.insertKey(15) 
heapObj.insertKey(5) 
heapObj.insertKey(4) 
heapObj.insertKey(45) 

print heapObj.extractMin(), 
print heapObj.getMin(), 
heapObj.decreaseKey(2, 1) 
print heapObj.getMin() 