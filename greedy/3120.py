start, end = list(map(int, input().split()))

def getMinCost(_gap : int):
    if _gap == 1 or _gap == 5:
        answer = 1
    elif _gap == 2 or _gap == 4 or _gap == 6 or _gap == 9:
        answer = 2
    elif _gap == 0:
        answer = 0
    else:
        answer = 3
    return answer

gap = end - start
if(gap < 0):
    gap = gap * -1

cost = 0

while( gap >= 10):
    cost += 1
    gap -= 10

cost += getMinCost(gap)

print(cost)
