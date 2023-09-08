matrix = []

#width, hight = input().split()

width = 10
hight = 10

class point:
    x = 0
    y = 0

start_pos = point()
start_pos.x = 1
start_pos.y = 1

prev_pos = point()
ant_pos = point()
prev_pos.x = 0
prev_pos.y = 0

isMoved = True

# init matrix
for h in range(0, width):
    matrix.append([])
    for w in range(0, hight):
        matrix[h].append(0)


# read maze
for i in range(10):
    row = input().split()
    #type casting
    for h in range(10):
        row[h] = int(row[h])
        matrix[i][h] = row[h]

# set ant
ant_pos = start_pos
matrix[ant_pos.x][ant_pos.y] = 9

# ant moves
while isMoved:
    if(matrix[ant_pos.x][ant_pos.y + 1] == 0):
        #back up prev
        isMoved = True
        #move right
        ant_pos.y +=1
        #record in matrix
        matrix[ant_pos.x][ant_pos.y] = 9
    elif(matrix[ant_pos.x+1][ant_pos.y] == 0):
        #back up prev
        isMoved = True
        #move down
        ant_pos.x +=1
        #record in matrix
        matrix[ant_pos.x][ant_pos.y] = 9
    else:
        isMoved = False

#if goal, go further
if(matrix[ant_pos.x][ant_pos.y + 1] == 2):
    #move right
    ant_pos.y +=1
    #record in matrix
    matrix[ant_pos.x][ant_pos.y] = 9
elif(matrix[ant_pos.x+1][ant_pos.y] == 2):
    #move down
    ant_pos.x +=1
    #record in matrix
    matrix[ant_pos.x][ant_pos.y] = 9
        
for i in range(0, width):
    for j in range(0, hight):
        print(matrix[i][j], end = " ")
    print("")