def selection_sort(a):
    n = len(a)
    for i in range(n):
        min_idx = i
        min_str = a[i]
        for j in range(i+1,n):
            if min_str > a[j]:
                min_idx = j
                min_str = a[j]
        if min_idx != i:
            temp = a[i]
            a[i] = a[min_idx]
            a[min_idx] = temp
    return a

a = ['gk','annamalai', 'arunsanthosh']
selection_sort(a)
print(a)