def magic_square(n):
    square = []
    for i in range(n):
        l = []
        for j in range(n):
            l.append(0)
        square.append(l)

    m = (n*((n**2)+1))/2
    
    row = n//2
    col = n-1

    count = 1
    num = n*n

    while count <= num:
        if (row == -1 and col == n):
          col = n -2
          row = 0
        else:
          if (col == n):
            col = 0
          if (row < 0):
            row = n - 1
        if(square[row][col] != 0):
            col = col - 2
            row = row + 1
            continue
        else:
          square[row][col] = count
          count += 1
        row -= 1
        col += 1

    for i in range(n):
      for j in range(n):
        print(square[i][j],end=" ")
      print()

if __name__ == "__main__":
    n = int(input("Enter a odd number for magiic square: "))
    magic_square(n)