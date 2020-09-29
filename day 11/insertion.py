class Node:

    def __init__(self,data):
        self.data = data
        self.next = None
    
class linkedlist:

    def __init__(self):
        self.head = None
    
    def push(self,new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def insertafter(self,prev_node, new_data):
        if prev_node is None:
            print("the given node must in linkedlist.")
            return
        
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def append(self,new_data):

        new_node = Node(new_data)

        if self.head is None:
            self.head = new_node
            return
        
        last = self.head
        while(last.next):
            last = last.next

        last.next = new_node

    def printList(self): 
        temp = self.head 
        while (temp): 
            print temp.data, 
            temp = temp.next