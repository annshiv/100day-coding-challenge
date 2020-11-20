class node:

    def __init__(self,value):
        self.value = value
        self.nextnode = None
    
class linkedlist:

    def __init__(self):
        self.head = None
    
    def printlist(self):
        temp = self.head 
        while (temp): 
            print (temp.data) 
            temp = temp.nextnode