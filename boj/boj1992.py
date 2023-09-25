from collections import deque
N = int(input())
matrix = list()
#matrix is
#       col0 col1 col2 ... colN
#row0
#row1
#row2
#row3
#row3
#i.e. matrix[row][col]

#blue : 1
#white : 0


num_blue = 0
num_white = 0

cols = list()

matrix = [[0 for i in range(N)] for i in range(N)]

for row in range(N):
    line = input()
    for col in range(N):
        matrix[row][col] = int(line[col])
#    for j in range(N):
#        cols.append(int(line[j]))
#    matrix.append(cols)

#print(matrix)

def printMatrix(row_begin, col_begin, _size):
    #x row
    #y col
    global matrix
    cur_row = row_begin
    cur_col = col_begin
    row_end = row_begin + _size
    col_end = col_begin + _size

    while cur_row < row_end:
        print(matrix[cur_row][cur_col], end=" ")
        
        cur_col += 1
        if cur_col == col_end:
            cur_col = col_begin
            cur_row += 1
            print()

def checkAllSame( row_begin, col_begin, _size):
    #print("check ", row_begin, ",", col_begin, "," ,_size)
    #x row
    #y col
    global matrix
    global num_blue
    global num_white
    val = matrix[row_begin][col_begin]
    ret = 1
    cur_row = row_begin
    cur_col = col_begin
    row_end = row_begin + _size
    col_end = col_begin + _size

    while cur_row < row_end:
        #print(matrix[cur_row][cur_col], end=" ")
        if val != matrix[cur_row][cur_col]:
            ret = 0
            break
        
        
        cur_col += 1
        if cur_col == col_end:
            cur_col = col_begin
            cur_row += 1

    if ret == 1:
        if val == 1:
            num_blue+=1
        else:
            num_white+=1
    return ret

#while True:
#    print("Usage : row col size")
#    args = list(map(int, input().split()))
#    printMatrix(args[0], args[1], args[2])
#    print(checkAllSame(args[0], args[1], args[2]))


#for i in range(N):
#    print(matrix[i])

def CountConfetti(row:int, col:int, _size:int):
    global num_white
    global num_blue
    #printMatrix(row, col, _size)
    #print()
    ret = checkAllSame(row,col,_size)
    if num_blue == 1:
        print("1", end="")
        num_blue = 0
    elif num_white == 1:
        print("0", end="")
        num_white = 0

    if(ret == 1):
        return
    else:
        next_size = _size//2
        print("(", end="")
        CountConfetti(row,col, next_size)
        CountConfetti(row,col+next_size, next_size)
        CountConfetti(row + next_size,col, next_size)
        CountConfetti(row+ next_size,col + next_size, next_size)
        print(")", end ="")

CountConfetti(0,0,N)

#print(num_white)
#print(num_blue)

#printMatrix(0,0,8)
