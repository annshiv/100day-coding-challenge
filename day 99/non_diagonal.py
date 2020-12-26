def sumOfParts(arr,N): 
	sum_part1, sum_part2, sum_part3, sum_part4 = 0, 0, 0, 0
	for i in range(N): 
		for j in range(N):
			if i + j < N - 1: 
				if(i < j and i != j and i + j): 
					sum_part1 += arr[i][j] 
				elif i != j: 
					sum_part2 += arr[i][j] 
			else: 
					sum_part3 += arr[i][j]  
					if i + j != N - 1 and i != j: 
						sum_part4 += arr[i][j] 
	return sum_part1 + sum_part2 + sum_part3 + sum_part4 
 
N = 4
arr = [[ 1, 2, 3, 4 ], 
	[ 5, 6, 7, 8 ], 
	[ 9, 10, 11, 12 ], 
	[ 13, 14, 15, 16 ]] 

print(sumOfParts(arr, N))