import sys

sys.setrecursionlimit(10000)
test_case = int(sys.stdin.readline())

def CountWorm():
    global matrix
    global col
    global row
    global worm_count

    for i in range(row):
        for j in range(col):
            return_code = DeleteSection(i,j)
            if( return_code == True ):
                worm_count += 1


def IsEnd(ri, ci):
    global matrix
    global col
    global row

    if ri == 0 or ri == row:
        return 

# ri : row index
# ci : col index
def DeleteSection(ri, ci):
    global matrix

    #print("ri:%d"%ri, "ci:%d"%ci)

    if matrix[ri][ci] == 0:
        return False

    matrix[ri][ci] = 0
    
    #left
    if ci >= 1:
        if matrix[ri][ci-1] == 1:
            DeleteSection(ri, ci-1)
    #right
    if ci < col-1:
        if matrix[ri][ci+1] == 1:
            DeleteSection(ri, ci+1)
    #down
    if ri < row-1:
        if matrix[ri+1][ci] == 1:
            DeleteSection(ri+1, ci)
    #up
    if ri >= 1:
        if matrix[ri-1][ci] == 1:
            DeleteSection(ri-1, ci)

    return True


def PrintMatrix():
    global matrix
    global col
    global row
    for ri in range(row):
        for ci in range(col):
            print(matrix[ri][ci], end="")
        print()
    

while test_case:
    test_case -= 1
    worm_count = 0

    col, row, cabbage_count = list(map(int, sys.stdin.readline().split()))

    #matrix 
    #    (row, col)
    #    ccccc
    #row 01234
    #row 1
    #row 2
    #row 3
    #row 4

    matrix = [[0 for _ in range(col)] for _ in range(row)]

    
    for _ in range(cabbage_count):
        cabbage_position_y, cabbage_position_x  = list(map(int, sys.stdin.readline().split()))
        matrix[cabbage_position_x][cabbage_position_y] = 1
        
    '''
    print("before@@@@@@@@")
    PrintMatrix()
    print("before@@@@@@@@")
    CountWorm()
    print("after@@@@@@@@")
    PrintMatrix()
    print("after@@@@@@@@")
    '''
    CountWorm()
    print(worm_count)


    
    

