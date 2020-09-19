string = 'AABCAAADA'
k = 3
lst = []
start = int(len(string) / k)
for i in range(start,len(string)+1,k):
    lst.append(string[:i])
print(lst)