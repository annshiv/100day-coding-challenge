from queue import Queue

def Print(Queue):
    while(not queue.empty()):
        print(queue.queue[0],end=", ")
        queue.get()
    
def reversequeue(queue):
    stack = []
    while(not queue.empty()):
        stack.append(queue.queue[0])
        queue.get()

    while(len(stack) != 0):
        queue.pop(stack[-1])
        stack.pop()