
#현재 주유소보다 싼 주유소까지만가는 거리만큼 주유하고 이동한다.

numOfGasstation = int(input())

distance = list(map(int, input().split()))
gasPrice = list(map(int, input().split()))

currStation = 0
currPrice = gasPrice[0]

totalPrice = 0

def GetCheaperStationIndex(_currPrice:int, _currStation:int):
    for i in range(_currStation, numOfGasstation):
        if _currPrice >  gasPrice[i]:
            return i
    return -1

def GetDistance(_from:int, _to:int):
    sum = 0
    for i in range(_from, _to):
        sum = sum + distance[i]
    return sum

while currStation != (numOfGasstation - 1):
    nextStation = GetCheaperStationIndex(currPrice, currStation)
    #print("from", currStation, "to", nextStation)
    if (nextStation == -1):
        nextStation = numOfGasstation - 1
    
    subDistance = GetDistance(currStation, nextStation)
    totalPrice += gasPrice[currStation] * subDistance
    currStation = nextStation
    currPrice = gasPrice[currStation]

print(totalPrice)


    