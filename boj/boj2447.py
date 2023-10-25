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


def GetMiddleList(_size:int):
    answer = list()
    starting_index = _size // 3
    ending_index = starting_index * 2
    for i in range(starting_index, ending_index):
        answer.append(i)

    return answer


#젤 큰 사각형에서 중간인가?
#x 를 3으로 나누고 y를 3으로 나눴을때, 몫이 중간범윈가?
#ex) 27 이라고한다면, 9 ~ 18 인가.
#그 다음 사각형에서 중간인가?
#그 다음...


def IsCenter(_x:int, _y:int, _size:int):
    #print(_x, _y)
    #중간인가? 중간이라면 찍기 중지
    middle_list = GetMiddleList(_size)
    #print(middle_list)
    if (_x in middle_list) and (_y in middle_list):
        #print(_x, _y, "both in middle")
        return True
    #그게 아니고, 마지막 깊이인가
    #그렇다면 중간이 아니므로 false 리턴
    elif _size == 3:
        return False
    else:
        smaller_size = _size//3
        new_pos = GetPositionInSmallerSqaure(_x, _y, _size)
        new_x = new_pos[0]
        new_y = new_pos[1]
        return IsCenter(new_x, new_y, smaller_size)
    

def GetPositionInSmallerSqaure(_x:int, _y:int, _current_size:int):
    step = _current_size // 3
    x, y = _x, _y
    while ( x >= step ):
        x -= step
    while ( y >= step ):
        y -= step
    return x, y
    

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
