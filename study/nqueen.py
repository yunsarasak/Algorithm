

#입력받고
n = int(input())

answer = list()

matrix = [[0 for _ in range(n)] for _ in range(n)]

def ClearMatrix():
    global matrix

    for i in range(n):
        for j in range(n):
            matrix[i][j] = 0

    return

def PrintMatrix():
    for i in range(n):
        for j in range(n):
            print(matrix[i][j], end=" ")
        print()
    
    return

def DoesAttackingVerticalOrHorizental(_row, _col):
    global n, matrix

    nReturn = 0
    
    for i in range(n):
        nReturn += matrix[_row][i]

    if nReturn > 0:
        return 1

    for j in range(n):
        nReturn += matrix[j][_col]
    
    if nReturn > 0:
        return 1
    
    return 0

def DoesAttackingDiagonal(_row, _col):
    global n, matrix
    
    #to right and down
    for i in range(n):
        next_row = _row+i
        next_col = _col+i
        if next_row < 0 or next_col < 0 or next_row >= n or next_col >= n:
            break
        if matrix[next_row][next_col] == 1:
            return 1

    #to left and up
    for i in range(n):
        next_row = _row-i
        next_col = _col-i
        if next_row < 0 or next_col < 0 or next_row >= n or next_col >= n:
            break
        if matrix[next_row][next_col] == 1:
            return 1

    #to right and up
    for i in range(n):
        next_row = _row-i
        next_col = _col+i
        if next_row < 0 or next_col < 0 or next_row >= n or next_col >= n:
            break
        if matrix[next_row][next_col] == 1:
            return 1

    #to left and down
    for i in range(n):
        next_row = _row+i
        next_col = _col-i
        if next_row < 0 or next_col < 0 or next_row >= n or next_col >= n:
            break
        if matrix[next_row][next_col] == 1:
            return 1
    
    return 0
            

def DoesThreat(_row:int, _col:int):
    nReturn = 0
    nReturn += DoesAttackingVerticalOrHorizental(_row, _col)
    nReturn += DoesAttackingDiagonal(_row, _col)

    return nReturn

def SetQueenTo(_row:int, _col:int):
    global matrix
    matrix[_row][_col] = 1

def GoBack(_row):
    for i in range(n):
        matrix[_row][i] = 0


def dfs(_row:int, _col:int):
    global n
    flag_answer = 0
    #범위를 넘어갔다면 fail return
    if _col == n:
        GoBack(_row)
        return

    #모든 퀸을 배치했다면 ( depth가 n이면 ) 리턴
    if _row == n:
        answer.append(matrix.copy())
        PrintMatrix()
        print()
        return

    #위협이 된다면 fail
    if DoesThreat(_row, _col):
        GoBack(_row)
        return
    else:
    #아니라면 배치
        SetQueenTo(_row, _col)

    #다음 퀸을 배치해본다.
    for i in range(n):
        dfs(_row+1, i)


    # if flag_answer == 0:
    #     GoBack(_row)
    return

for j in range(n):
    dfs(0,j)

print(len(answer))

