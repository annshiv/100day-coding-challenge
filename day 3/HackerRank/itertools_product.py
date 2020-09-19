# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product
A = list(map(int,input().split()))
B = list(map(int,input().split()))
result = list(product(A,B))
res = ""
for i in result:
    res += str(i)
    res += " "
print(res)