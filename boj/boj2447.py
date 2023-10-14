def PrintSquare(_flag:any):
    print("***")
    print("* *")
    print("***", end="")


def Maximum3Multiple(_num:int):
    answer = 1
    while(True):
        if _num > answer * 3:
            break
        else:
            answer *= 3

    return answer
        


def IsCenter(_x:int, _y:int):
    #중간인가? 중간이라면 찍기 중지
    print(_x, _y)
    if (_x == 1) and (_y == 1):
        return True
    elif ((_x == 0) or (_x == 2)) and ((_y == 0) or (_y == 2)):
        return False
    else:
        return IsCenter( _x - Maximum3Multiple(_x), _y - Maximum3Multiple(_y) )
    

N = int(input())

for i in range(N):
    for j in range(N):
        if IsCenter(i,j):
            continue
        else:
            print("*", end="")
