def createstack():
    stack = []
    return stack

def size(stack):
    return len(stack)

def isempty(stack):
    if size(stack) == 0:
        return True
    
def push(stack,item):
    stack.append(item)

def pop(stack):
    return stack.pop()

def reversea(string):
    n = len(string)

    stack = createstack()

    for i in range(0,n):
        push(stack,string[i])

    string = ""
    for i in range(0,n,1):
        string +=  pop(stack)    
    return string

string = "Annamalai"
string = reversea(string)
print(string)
