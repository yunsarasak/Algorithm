matrix = []

for i in range(0, 19):
    matrix.append([])
    for j in range(0, 19):
        matrix[i].append(0)

for i in range(19):
    listInput = input().split()
    for j in range(19):
        matrix[i][j] = int(listInput[j])

n = int(input())

for i in range(n):
    x, y = input().split()
    x = int(x)
    y = int(y)
    x-=1
    y-=1
    for j in range(19):
        if matrix[x][j] == 1:
            matrix[x][j] = 0
        else:
            matrix[x][j] = 1

        if matrix[j][y] == 1:
            matrix[j][y] = 0
        else:
            matrix[j][y] = 1

for i in range(0, 19):
    for j in range(0, 19):
        print(matrix[i][j], end = " ")
    print("")