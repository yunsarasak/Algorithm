import sys

sys.setrecursionlimit(10**9)

row, col = list(map(int, input().split()))

matrix = list()

def PrintMatrix():
    global row, col, matrix

    for i in range(row):
        print(matrix[i])

    return

directions = [
    [-1, -1],
    [-1, 0],
    [-1, 1],
    [0, -1],
    #[0, 0],
    [0, 1],
    [1, -1],
    [1, 0],
    [1, 1]
]

def IsThereCharacter(_row:int, _col:int):
    global matrix

    if matrix[_row][_col] == 0:
        return 0
    else:
        return 1

def EreaseCharacterAt(_row:int, _col:int):
    global matrix
    global row, col
    global directions

    if IsThereCharacter(_row, _col) == 0:
        return
    else:
        matrix[_row][_col] = 0

    for dir in directions:
        if _row+dir[0] < 0 or _row+dir[0] >= row:
            continue

        if _col+dir[1] < 0 or _col+dir[1] >= col:
            continue

        if matrix[_row+dir[0]][_col+dir[1]] == 1:
            EreaseCharacterAt(_row+dir[0], _col+dir[1])

    return

for i in range(row):
    single_row = list(map(int, input().split()))

    matrix.append(single_row)

CharacterCount = 0

# print("before")
# PrintMatrix()

for i in range(row):
    for j in range(col):
        if IsThereCharacter(i, j):
            EreaseCharacterAt(i, j)
            CharacterCount += 1

# print("after")
# PrintMatrix()

print(CharacterCount)