numOfTopping = int(input())
doughPrice, toppingPrice = list(map(int, input().split()))

doughCalorie = int(input())
toppingCalorie = []

for i in range( numOfTopping ):
    toppingCalorie.append(int(input()))

def getToppingCalories( _toppingList : list, _toppingPrcie : int, _toppingCount : int):
    sum = 0
    for i in range(_toppingCount):
        sum += _toppingList[i]

    return sum

#print(toppingCalorie)
toppingCalorie.sort(reverse=True)
#print(toppingCalorie)


currentAvg = doughCalorie // doughPrice

toppingCount = 0
while True:
    nextAvg = (doughCalorie + getToppingCalories( toppingCalorie, toppingPrice, (toppingCount + 1))) // (doughPrice + toppingPrice * (toppingCount + 1))
    #print(nextAvg)
    #print(currentAvg)

    if currentAvg > nextAvg:
        break

    toppingCount += 1

    if toppingCount == len(toppingCalorie):
        break

    currentAvg = nextAvg

print(currentAvg)


    
