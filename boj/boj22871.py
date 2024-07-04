import sys

sys.setrecursionlimit(10**9)

num_of_stones = int(input())

stepping_stones = list(map(int, input().split()))

def SetNewRecord(_new_record:int):
    global max
    max = _new_record
    return

def GetDifference(_a:int, _b:int):
    if _a > _b:
        return _a - _b
    else:
        return _b - _a

def GetForceNeeded(_from:int, _to:int):
    global stepping_stones

    _from -= 1
    _to -= 1
    
    #print("(%d - %d) * (1+|%d - %d|)"%(_to, _from, stepping_stones[_from], stepping_stones[_to]))
    return (_to - _from) * (1 + GetDifference(stepping_stones[_from], stepping_stones[_to]))

# while True:
#     begin, end = list(map(int, input().split()))

#     force_needed = GetForceNeeded(begin, end)
#     print(force_needed)


# current_position = 1

# max_force = GetForceNeeded(current_position, current_position+1)

# current_position += 1

# while current_position != num_of_stones:
#     force_to_next_step = GetForceNeeded(current_position, current_position+1)

#     if max_force < force_to_next_step:
#         max_force = force_to_next_step

#     current_position += 1

# print(max_force)

answer = sys.maxsize

def FindWayRightEnd(_pos:int, _max:int):#, _path:list):
    global num_of_stones, answer

    if _pos > num_of_stones:
        return

    #_path.append(_pos)

    if _pos == num_of_stones:
        if answer > _max:
            answer = _max
            #print(_path)
            # _path.pop()
            return
    
    distance = 1
    while (_pos+distance) <= num_of_stones:
        force_to_move = GetForceNeeded(_pos, _pos+distance)

        if force_to_move > answer:
            # _path.pop()
            return

        new_max = _max

        if (force_to_move > _max) or (_max == -1):
            new_max = force_to_move

        FindWayRightEnd( _pos+distance, new_max)#, _path)
        distance += 1
    
    # _path.pop()
    return

    
        
# 1번 돌부터 step가능한 다음 돌로 이동해본다
current_pos = 1
#path = list()

max = -1

FindWayRightEnd(current_pos, max)#, path)

print(answer)
