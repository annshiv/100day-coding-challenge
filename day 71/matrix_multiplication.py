MAX = 100
i = 0
j = 0
k = 0

def multiplyMatrixRec(row1, col1, A, row2, col2, B, C): 
	global i 
	global j 
	global k 
 
	if (i >= row1): 
		return

	if (j < col2): 
		if (k < col1): 
			C[i][j] += A[i][k] * B[k][j] 
			k += 1
			multiplyMatrixRec(row1, col1, A, 
							row2, col2,B, C) 

		k = 0
		j += 1
		multiplyMatrixRec(row1, col1, A, 
						row2, col2, B, C) 

	j = 0
	i += 1
	multiplyMatrixRec(row1, col1, A, 
					row2, col2, B, C) 
def multiplyMatrix(row1, col1, A, row2, col2, B): 
	if (row2 != col1): 
		print("Not Possible") 
		return

	C = [[0 for i in range(MAX)] 
			for i in range(MAX)] 
	multiplyMatrixRec(row1, col1, A, row2, col2, B, C) 
	
	for i in range(row1): 
		for j in range(col2): 
			print( C[i][j], end = " ") 
		print() 

# Driver Code 
A = [[1, 2, 3], 
	[4, 5, 6], 
	[7, 8, 9]] 
B = [[1, 2, 3], 
	[4, 5, 6], 
	[7, 8, 9]] 

row1 = 3
col1 = 3
row2 = 3
col2 = 3
multiplyMatrix(row1, col1, A, row2, col2, B) 
