##def getIndex(_list : list, _num : int):
##    listLength = len(_list)
##    for i in range(listLength):
##        if _list[i] == _num:
##            return i
#
##read input
#n = int(input())
#
#numList = list(map(int,input().split()))
#
##type casting
##for i in range(n):
##    numList[i] = int(numList[i])
#
##copy list
#copyOfList = sorted(numList)
#
##sort
##numList.sort()
#
#for i in range(n):
#    #result = getIndex(numList, copyOfList[i])
#    print(copyOfList.index(numList[i]), end=" ")
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@ previous attempt

# counting sort

#read input size
inputSize = int(input())

# define count array
countArray = [0 for i in range(500001)]

# read inputs
numList = list(map(int, input().split()))

for i in range(inputSize):
    #read 1 num
    num = numList[i]
    #count
    countArray[num] += 1

# set count array into cumulative count array
for i in range(1,500001):
    countArray[i] += countArray[i-1]

# print index
for i in range(len(numList)):
    print(countArray[numList[i]] - 1, end = " ")

#print(countArray)