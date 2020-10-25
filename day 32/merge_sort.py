def merge_sort(a):
    if len(a) > 1:
        mid = len(a)//2
        lefthalf = a[:mid]
        righthalf = a[mid:]

        merge_sort(lefthalf)
        merge_sort(righthalf)

        i = 0
        j = 0
        k = 0

        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                a[k] = lefthalf[i]
                i += 1
            
            else:
                a[k] = righthalf[j]
                j += 1
            
            k += 1
        while i < len(lefthalf):
            a[k] = lefthalf[i]
            i += 1
            k += 1
        
        while j < len(righthalf):
            a[k] = righthalf[j]
            j += 1
            k += 1

a = [233,42,3,2,3,23,3,45,23,42,3,2234]
merge_sort(a)
print(a)