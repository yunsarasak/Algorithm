import sys

N = int(sys.stdin.readline())
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


num_plus_one = 0
num_zero = 0
num_minus_one = 0

for i in range(N):
    cols = list(map(int, sys.stdin.readline().split()))
    matrix.append(cols)


def printMatrix(row_begin, col_begin, _size):
    #x row
    #y col
    global matrix
    cur_row = row_begin
    cur_col = col_begin
    row_end = row_begin + _size
    col_end = col_begin + _size

    while cur_row < row_end:
        #print(matrix[cur_row][cur_col], end=" ")
        
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
    global num_plus_one
    global num_zero
    global num_minus_one
    val = matrix[row_begin][col_begin]
    ret = 1
    cur_row = row_begin
    cur_col = col_begin
    row_end = row_begin + _size
    col_end = col_begin + _size

    while cur_row < row_end:
        #print(matrix[cur_row][cur_col], end=" ")
        #print("val, matrix[x][y] == ", val, ",", matrix[cur_row][cur_col])
        if val != matrix[cur_row][cur_col]:
            ret = 0
            break
        
        
        cur_col += 1
        if cur_col == col_end:
            cur_col = col_begin
            cur_row += 1

    if ret == 1:
        if val == 1:
            num_plus_one+=1
        elif val == 0:
            num_zero+=1
        else:
            num_minus_one+=1

    return ret

#while True:
#    print("Usage : row col size")
#    args = list(map(int, sys.stdin.readline().split()))
#    printMatrix(args[0], args[1], args[2])
#    print(checkAllSame(args[0], args[1], args[2]))


        

#for i in range(N):
#    print(matrix[i])

def CountConfetti(row:int, col:int, _size:int):
    ret = checkAllSame(row,col,_size)
    #print()
    #printMatrix(row,col,_size)
    if(ret == 1):
        return
    else:
        next_size = _size//3
        CountConfetti(row,col, next_size)
        CountConfetti(row + next_size,col, next_size)
        CountConfetti(row + 2*next_size,col, next_size)

        CountConfetti(row,col+next_size, next_size)
        CountConfetti(row+next_size,col+next_size, next_size)
        CountConfetti(row+2*next_size,col+next_size, next_size)

        CountConfetti(row,col+2*next_size, next_size)
        CountConfetti(row+next_size,col+2*next_size, next_size)
        CountConfetti(row+2*next_size,col+2*next_size, next_size)

CountConfetti(0,0,N)

print(num_minus_one)
print(num_zero)
print(num_plus_one)
#printMatrix(0,0,N)
