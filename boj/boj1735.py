import sys
import math

def GetGCD( _a:int, _b:int ):
    remain = 1

    if ( _a > _b ):
        min = _b
        max = _a
    else:
        min = _a
        max = _b

    divisor = min
    dividend = max
    remain = max % min
    ##print( dividend, "%", divisor, "=", remain)

    while( remain ):
        dividend = divisor
        divisor = remain
        remain = min % divisor
        #print( dividend, "%", divisor, "=", remain)

    return divisor


A, B = list(map( int, sys.stdin.readline().split()))

C, D = list(map( int, sys.stdin.readline().split()))

_B = B 
_D = D

A = A * D
B = B * D

#print("first : ", A)
#print("first : ", B)

C = C * _B
D = D * _B
#print("secod : ", C)
#print("secod : ", D)

#print(A)
#print(C)

answerMom = B

#print(A, "+", C, "=", A+C)
answerSon = A+C
#print(A, "+", C, "=", answerSon)


#get GCD
#using euclidian algorithm

gcd1 = GetGCD(answerMom, answerSon)
gcd2 = math.gcd(answerMom, answerSon)

print(gcd1)
print(gcd2)

answerMom = int(answerMom / gcd1)
answerSon = int(answerSon / gcd1)

print(answerSon, answerMom)