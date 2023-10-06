#cheat sheet
#https://kyun2da.github.io/2020/08/30/BinomialCoefficient/

import sys

sys.setrecursionlimit(4000000)

def power( _base:int, _exp:int ):
    global C
    #print("base : ", _base, "_exp :", _exp)
    if _exp == 0:
        return 1
    elif _exp == 1:
        return (_base % C)
    
    k = power(_base, _exp//2)
    #print(k)
    if _exp % 2 == 0:
        return (k * k) % C
    else:
        return (_base * (k * k)) % C

N, K = list(map(int,input().split()))

def combi(n:int, m:int):
    if (m == 0) or (m == n):
        return 1
    else:
        return combi(n-1, m-1) + combi(n-1, m)

answer = combi(N, K)

answer = answer % 1000000007

print(answer)