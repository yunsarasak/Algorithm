import sys
#import math

#def PrintSquare(_flag:any):
#    print("***")
#    print("* *")
#    print("***", end="")
#
#
#def GetMaxDepth(_num:int):
#    answer = 1
#    while (True):
#        powed = math.pow(3, answer)
#        if powed == _num:
#            return answer
#        elif powed > _num:
#            return -1
#        else:
#            answer += 1

#middle = dict()
#
#
#
#def GetMiddleList(_size:int):
#    global middle
#    str_size = str(_size)
#    if str_size in middle:
#        return middle[str_size]
#    answer = list()
#    starting_index = _size // 3
#    ending_index = starting_index * 2
#    for i in range(starting_index, ending_index):
#        answer.append(i)
#
#    middle[str_size] = answer
#    return answer


#젤 큰 사각형에서 중간인가?
#x 를 3으로 나누고 y를 3으로 나눴을때, 몫이 중간범윈가?
#ex) 27 이라고한다면, 9 ~ 18 인가.
#그 다음 사각형에서 중간인가?
#그 다음...


def IsCenter(_x:int, _y:int, _size:int):
    #중간인가? 중간이라면 찍기 중지
    step = _size//3
    #print(_x, _y)
    #print(step)

    #print(middle_list)
    #print("is ", _x, ",", _y, "from ", step, "to", 2*step-1)
    if ( (step <= _x) and (_x <= 2*step-1) ) and (  (step <= _y) and (_y <= 2*step-1) ):
        #print(_x, _y, "both in middle")
        return True
    else:
        if _size == 3:
            return False
        return IsCenter(_x%step, _y%step, _size//3)
    

#def GetPositionInSmallerSqaure(_x:int, _y:int, _current_size:int):
#    step = _current_size // 3
#    x, y = _x, _y
#    while ( x >= step ):
#        x -= step
#    while ( y >= step ):
#        y -= step
#    return x, y

N = int(sys.stdin.readline())
#N = int(input())

#max_detph = GetMaxDepth(N)
#print("max depth : ", max_detph)

#middle_list = GetMiddleList(N)
#print(middle_list)



for i in range(N):
    for j in range(N):
        if IsCenter(i, j, N) == True:
            print(" ", end="")
        else:
            print("*", end="")
    print()
