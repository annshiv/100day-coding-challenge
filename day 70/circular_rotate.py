MAX = 1000
def isPermutedMatrix(mat, n) : 
	str_cat = "" 
	for i in range(n) : 
		str_cat = str_cat + "-" + str(mat[0][i]) 
	str_cat = str_cat + str_cat 
	for i in range(1, n) : 
		curr_str = "" 
		
		for j in range(n) : 
			curr_str = curr_str + "-" + str(mat[i][j]) 

		if (str_cat.find(curr_str)) : 
			return True
			
	return False

# Driver code 
if __name__ == "__main__" : 
	n = 4
	mat = [[1, 2, 3, 4], 
		[4, 1, 2, 3], 
		[3, 4, 1, 2], 
		[2, 3, 4, 1]] 
	
	if (isPermutedMatrix(mat, n)): 
		print("Yes") 
	else : 
		print("No") 
