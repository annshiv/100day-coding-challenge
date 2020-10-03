head = None

class Node:

    def __init__(self,data):
        self.data = data
        self.next = None
    
def segrateEvenOdd():
    global head

    evenstart = None
    evenend = None
    oddstart = None
    oddend = None
    currNode = head
    while(currNode != None):
        val = currNode.data

        if(val % 2 == 0):
            if(evenstart == None):
                evenstart = currNode
                evenend = evenstart
            else:
                evenend.next = currNode
                evenend = evenend.next
        else:
            if(oddstart == None):
                oddstart = currNode
                oddend = oddstart
            else:
                oddend.next = currNode
                oddend = oddend.next
        currNode = currNode.next
    if(oddstart == None or evenstart == None):
        return
    
    evenend.next = oddstart
    oddend.next = None

    head = evenstart
def push(new_data):
    global head

    new_node = Node(new_data)
    new_node.next = head
    head = new_node

def printlist():
    global head
    node = head
    while (node != None):
        print(node.data, end=" ")
        node = node.next
    print()

push(11)
push(10)
push(9)
push(6)
push(3)
push(1)
push(0)
print("Original linked list")
printlist()

segrateEvenOdd()

print("Modified Linked list")
printlist()