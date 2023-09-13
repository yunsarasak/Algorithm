import sys
import time

start = time.time()



A, B = list(map( int, sys.stdin.readline().split()))

C, D = list(map( int, sys.stdin.readline().split()))

_B = B 
_D = D

A = A * D
B = B * D

C = C * _B
D = D * _B

answerMom = B

answerSon = A + C

if answerMom == 1:
    print( answerSon, answerMom )
else:
    flag = 1
    while flag:
        for i in range(min(answerMom, answerSon), 0, -1):
            #print(i)
            if i == 1:
                flag = 0
                break
            if (answerMom % i == 0) and (answerSon % i == 0):
                #print( answerMom ,"divide by", i, end="")
                answerMom = int(answerMom / i)
                #print( " ",answerMom)

                #print( answerSon ,"divide by", i, end="")
                answerSon = int(answerSon / i)
                #print(answerSon)

                i = min(answerMom, answerSon)


    if answerMom % answerSon == 0:
        answerMom = int(answerMom / answerSon)
        answerSon = int(answerSon / answerSon)

    if answerSon % answerMom == 0:
        answerSon = int(answerSon / answerMom)
        answerMom = int(answerMom / answerMom)
            
    print( int(answerSon), int(answerMom) )


end = time.time()
print(end - start, "sec")