def binary(arr,x):
    for i in range(0,len(arr)):
        if (arr[i]==x):
            return i
    return -1

if __name__ == "__main__":    
    arr = list(map(int,input().split(" ")))
    x = int(input("Enter value to find : "))
    print(binary(arr,x))
