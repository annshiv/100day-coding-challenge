import heapq

lst = [5, 7, 9, 1, 3] 
heapq.heapify(lst)
heapq.heappush(lst,4)
print("Print list after a push :",end=" ")
print(list(lst))
heapq.heappop(lst)
print("Print list after a pop :",end=" ")
print(list(lst))
heapq.heappushpop(lst,2)
print("Print list after a pushpop :",end=" ")
print(list(lst))

heapq.heapreplace(lst,10)
heapq.heapify(lst)
print("Print list after a replace :",end=" ")
print(list(lst))

#nlargest function
print("Largest three numbers in list :",end=" ")
print(heapq.nlargest(3,lst))

#nsmallest function
print("Smallest three numbers in list :",end=" ")
print(heapq.nsmallest(3,lst))
