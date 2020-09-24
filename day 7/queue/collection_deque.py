from collections import deque

q = deque()

#adding elements in queue
q.append('a')
q.append('b')
q.append('c')

print("Initial queue :",end=" ")
print(q)

#remove elements from the queue

q.popleft()
q.popleft()
q.popleft()

print("Remove elements from the queue :",end=" ")
print(q)