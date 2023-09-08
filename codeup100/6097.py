matrix = []

width, hight = input().split()

width = int(width)
hight = int(hight)

barCount = int(input())

# init matrix
for h in range(0, width):
    matrix.append([])
    for w in range(0, hight):
        matrix[h].append(0)

# set bar position
for i in range(barCount):
    length, direction, x, y = input().split()
    length = int(length)
    direction = int(direction)
    
    x = int(x)
    y = int(y)
    x-=1
    y-=1

    #matrix[x][y] = 2

    if direction == 0:
        #set horizontal
        for h in range(length):
            matrix[x][y+h] = 1
    else:
        #set vertical
        for w in range(length):
            matrix[x+w][y] = 1
        
for i in range(0, width):
    for j in range(0, hight):
        print(matrix[i][j], end = " ")
    print("")