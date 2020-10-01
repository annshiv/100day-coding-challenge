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
        s = set()
        temp = self.head
        while(temp):
            if (temp in s):
                return True
            s.add(temp)
            temp = temp.next
        return False

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
    