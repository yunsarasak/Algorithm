days, rooms = list(map(int, input().split()))

reservedList = list()

#reserved [ room ] [ day ]

for i in range(rooms):
    reservedList.append([])

for i in range(days):
    reserveString = input()

    for j in range(len(reserveString)):
        if reserveString[j] == "X":
            reservedList[j].append(0)
        else:
            reservedList[j].append(1)

start, end = list(map(int, input().split()))

start -=1
end -=1

#print(reservedList)

reservedCumulative = reservedList.copy()

#set cumulative sum
for i in range(rooms):
    for j in range(days):
        if( reservedCumulative[i][j - 1] > 0 ) and (reservedCumulative[i][j] == 1 ):
            reservedCumulative[i][j] = reservedCumulative[i][j - 1] +1

#print(reservedCumulative)

currentDay = end
currentRoom = end
jumpCount = 0

#get last room
roomIndex = 0

for currentRoom in range( rooms ):
    if( reservedCumulative[currentRoom][end - 1] > reservedCumulative[roomIndex][end - 1]):
        #print(reservedCumulative[currentRoom][end - 2], "<", reservedCumulative[roomIndex][end - 1], sep = " ")
        roomIndex = currentRoom

#print(reservedCumulative[roomIndex][end - 1])
#print("day : ", currentDay)
#print("room : ", roomIndex)

if reservedCumulative[roomIndex][end - 1] == 0:
    jumpCount = -1
else:
    #print("first selected room : ", roomIndex)
    for currentDay in range(end - 1, start, -1):
        #if there is reamining day, don't jump
        if reservedCumulative[roomIndex][currentDay] > 1:
            continue
        
        #if there isn't, jumps
        #select largest remaing day
        nextDay = currentDay - 1
        for currentRoom in range( rooms ):
            if( reservedCumulative[currentRoom][nextDay] > reservedCumulative[roomIndex][nextDay]):
                roomIndex = currentRoom
        

        #if nowhere to go, return -1
        if( reservedCumulative[roomIndex][nextDay] == 0):
            jumpCount = -1
            break

        #print("current day : ", currentDay)
        #print("current room : ", currentRoom)
        #print("jumps to ", roomIndex)

        #else counts
        jumpCount += 1
                

print(jumpCount)


# check possiblity
# bit or for all rooms and bit and for all days
#possiblitiy = [ 0 for i in range(days)]

#if there any unreserved room, set 1
#for i in range(days):
#    for j in range(rooms):
#        possiblitiy[j] = reservedList[i][j] | possiblitiy[j]

##print(possiblitiy)
#canBeBooked = 1
#for i in range(start, end - 1):
#    canBeBooked = canBeBooked & possiblitiy[i]
#    #print(canBeBooked, "and", "possiblitiy[",i,"]", " = ", canBeBooked & possiblitiy[i] )
## check possiblity done
#
#
##if can be booked, calc jump counts
#jumpCount = 0
#
##check only room
#
##print result
#if canBeBooked == 0:
#    print("-1")
#else:
#    print(jumpCount)
