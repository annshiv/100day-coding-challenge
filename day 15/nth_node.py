class Node():
     
     def __init__(self,data):
         self.data = data
         self.next = None

class linkedlist():

    def __init__(self):
        self.head = None
    
    def push(self,new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
    
    def getNth(self,index):
        current = self.head
        count = 0
    
        while(current):
            if (count == index):
                return current.data
            count += 1
            current = current.next
        assert(False)
        return 0
    
if __name__=='__main__': 
  
    llist = linkedlist()
    llist.push(1); 
    llist.push(4); 
    llist.push(1); 
    llist.push(12); 
    llist.push(1); 
  
    n = 4
    print ("Element at index {} is : {}".format(n,llist.getNth(n)))