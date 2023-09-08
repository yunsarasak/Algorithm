#read input count
inputCount = int(input())

#read list
numList = list(map(int, input().split()))

for i in range(inputCount):
    print(numList[inputCount - 1 - i], end = " ")
    