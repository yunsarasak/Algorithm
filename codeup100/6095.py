matrix = []

for i in range(0, 19):
    matrix.append([])
    for j in range(0, 19):
        matrix[i].append(0)

n = int(input())

for i in range(n):
    x, y = input().split()
    x = int(x)
    y = int(y)
    x-=1
    y-=1
    matrix[x][y] = 1

for i in range(0, 19):
    for j in range(0, 19):
        print(matrix[i][j], end = " ")
    print("")