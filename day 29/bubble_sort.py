
def bubble_sort(a):
    for i in range(0,len(a)-1):
        for j in range(0,len(a)-1):
            if a[j] > a[j+1]:
                temp = a[j]
                a[j] = a[j+1]
                a[j+1] = temp
a = [1.345,56,2,45,6,3]
bubble_sort(a)
print(a)