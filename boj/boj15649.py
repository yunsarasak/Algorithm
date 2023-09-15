N, M = list(map( int, input().split()))

def backTracking(_answer:list, _depth:int):
    if _depth != M:
        #dive 1 depth
        for i in range( _answer(_depth), N+1):
            _answer.append(i)
            backTracking(_answer, _depth+1)
            _answer.remove(i)
    else:
        print( _answer )

answer = list()

answer.append(1)

backTracking(answer, 1)


