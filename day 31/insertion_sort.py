def insertion_sort(a):
    n = len(a)
    for  i in range(1,n):
        key = a[i]
        j = i - 1
        while j>=0 and key < a[j]:
            a[j+1] = a[j]
            j -= 1
        a[j+1] = key

a = [234,35,2,3,4,32,4,3,45,3,23,3,4]
insertion_sort(a)
print(a)