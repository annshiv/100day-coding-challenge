a = [23,2345,64,21,35,12,34,2]
def selection_sort(a):
    for i in range(len(a)):
        min_indx = i
        for j in range(i+1,len(a)):
            if a[min_indx] > a[j]:
                min_indx = j            
            a[i],a[min_indx] = a[min_indx],a[i] 
selection_sort(a)
print(a)