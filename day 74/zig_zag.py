matrix =[ 
			[ 1, 2, 3,], 
			[ 4, 5, 6 ], 
			[ 7, 8, 9 ], 
		] 
rows=3
columns=3
	
solution=[[] for i in range(rows+columns-1)] 

for i in range(rows): 
	for j in range(columns): 
		sum=i+j 
		if(sum%2 ==0): 
			solution[sum].insert(0,matrix[i][j]) 
		else: 
			solution[sum].append(matrix[i][j]) 
 
for i in solution: 
	for j in i: 
		print(j,end=" ") 