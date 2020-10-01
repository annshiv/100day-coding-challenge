class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = None
    
    def push(self,new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
    
    def printlist(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next
    
    def detectloop(self):
        slow_p = self.head
        fast_p = self.head
        while(slow_p and fast_p and fast_p.next):
            slow_p = slow_p.next
            fast_p = fast_p.next.next
            if (slow_p == fast_p):
                return True
    
if __name__ == "__main__":
    l = LinkedList()
    l.push(20)
    l.push(4) 
    l.push(15) 
    l.push(10)
    l.head.next.next.next.next = l.head
    if (l.detectloop()):
        print("Loop found")
    else:
        print("No loop")     
    