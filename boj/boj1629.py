A, B, C = list(map(int, input().split()))

def power( _base:int, _exp:int ):
    global A
    global B
    global C
    if _exp == 0:
        return 1
    elif _exp == 1:
        return _base
    
    if _exp % 2 == 0:
        return power( ... )