def InsertionSortRecursive(a,n):
    if n <= 0:
        return
    InsertionSortRecursive(a,n-1)
    last = a[n-1]
    j = n-2

    while (j>=0 and a[j] > last):
        a[j+1] = a[j]
        j -= 1

    a[j+1] = last

a = [234,42,3,5,22,3,2,31]
InsertionSortRecursive(a,len(a))
print(a)