# Node class 
class Node: 
	def __init__(self, data): 
		self.data = data 
		self.next = None

class LinkedList: 
	def __init__(self): 
		self.head = None

	def pairwiseSwap(self): 
		temp = self.head 
		if temp is None: 
			return
		while(temp is not None and temp.next is not None): 
			if(temp.data == temp.next.data): 
				temp = temp.next.next
			else: 
				temp.data, temp.next.data = temp.next.data, temp.data 
				temp = temp.next.next
	def push(self, new_data): 
		new_node = Node(new_data) 
		new_node.next = self.head 
		self.head = new_node 
	def printList(self): 
		temp = self.head 
		while(temp): 
			print(temp.data) 
			temp = temp.next
llist = LinkedList() 
llist.push(5) 
llist.push(4) 
llist.push(3) 
llist.push(2) 
llist.push(1) 

print("Linked list before calling pairWiseSwap() ")
llist.printList() 

llist.pairwiseSwap() 

print("\nLinked list after calling pairWiseSwap()")
llist.printList() 
