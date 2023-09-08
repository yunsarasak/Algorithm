n = int(input())
remainingChange = n

#탐욕적 선택 속성을 갖는가?
#거스름돈의 역순으로
#가장 많이 선택하는 것이 최적해 ( 최소 거스름돈 )를 만족한다.

result = 0

while (remainingChange != 0):
    if remainingChange >= 50000:
        remainingChange -= 50000
    elif remainingChange >= 10000:
        remainingChange -= 10000
    elif remainingChange >= 5000:
        remainingChange -= 5000
    elif remainingChange >= 1000:
        remainingChange -= 1000
    elif remainingChange >= 500:
        remainingChange -= 500
    elif remainingChange >= 100:
        remainingChange -= 100 
    elif remainingChange >= 50:
        remainingChange -= 50 
    elif remainingChange >= 10:
        remainingChange -= 10 

    result += 1

print(result)
