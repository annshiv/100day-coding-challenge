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
    
    def detect_remove_loop(self):
        if self.head is None:
            return False
        if self.head.next is None:
            return False
        
        slow = self.head
        fast = self.head

        slow = slow.next
        fast = fast.next.next

        while(fast is not None):
            if fast.next is None:
                break
            if slow == fast:
                break
            slow = slow.next
            fast = fast.next.next

        if slow == fast:
            slow = self.head
            while(slow.next != fast.next):
                slow = slow.next
                fast = fast.next
            fast.next = None

    def printlist(self):
        temp = self.head
        while(temp):
            print(temp.data, end=" ")
            temp = temp.next

llist = linkedlist() 
llist.head = Node(50) 
llist.head.next = Node(20) 
llist.head.next.next = Node(15) 
llist.head.next.next.next = Node(4) 
llist.head.next.next.next.next = Node(10) 
  
llist.head.next.next.next.next.next = llist.head.next.next
  
llist.detect_remove_loop()
  
print("Linked List after removing loop")
llist.printlist() 