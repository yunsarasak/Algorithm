#https://codeup.kr/problem.php?id=4816

#read input
T = int(input())
remainTime = T


a = 300
b = 60
c = 10

countA = 0
countB = 0
countC = 0

while remainTime >= 10:
    if ( remainTime >= a ):
        countA += 1
        remainTime -= a
    elif ( remainTime >= b ):
        countB += 1
        remainTime -= b
    elif ( remainTime >= c ):
        countC += 1
        remainTime -= c

if (remainTime != 0):
    print("-1")
else:
    print(countA, countB, countC, sep=" ")


