A, B, C = list(map(int, input().split()))

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


print(power(A, B))