n = 4
def count(arr): 
	diag1 = 0; diag2 = 0; row = 0
	col = 0; count = 0; j = n - 1
	
	for i in range(n): 
		diag1 += arr[i][i] 
		diag2 += arr[i][j] 
		j -= 1
	for i in range(n): 
		row = 0; col = 0
		
		for j in range(n): 
			row += arr[i][j] 
		
		for j in range(n): 
			col += arr[j][i] 
		
		if ((row == diag1) or (row == diag2)): 
			count += 1
		
		if ((col == diag1) or (col == diag2)): 
			count += 1
	
	return count 


arr = [[ 7, 2, 3, 5 ], 
	[ 4, 5, 6, 3 ], 
	[ 7, 9, 10, 12 ], 
	[ 1, 5, 4, 3 ] ] 
print(count(arr))