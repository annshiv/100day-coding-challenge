SIZE = 10 
def sortMat(mat, n) :  
	temp = [0] * (n * n) 
	k = 0 
	for i in range(0, n) : 
		
		for j in range(0, n) : 
			
			temp[k] = mat[i][j] 
			k += 1
	temp.sort() 
	k = 0
	
	for i in range(0, n) : 
		
		for j in range(0, n) : 
			mat[i][j] = temp[k] 
			k += 1

def printMat(mat, n) : 
	
	for i in range(0, n) : 
		
		for j in range( 0, n ) : 
			
			print(mat[i][j] , end = " ") 
			
		print() 
mat = [ [ 5, 4, 7 ], 
		[ 1, 3, 8 ], 
		[ 2, 9, 6 ] ] 
n = 3

print( "Original Matrix:") 
printMat(mat, n) 

sortMat(mat, n) 

print("\nMatrix After Sorting:") 
printMat(mat, n) 
