num_of_stones = int(input())

stepping_stones = list(map(int, input().split()))


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

while True:
    begin, end = list(map(int, input().split()))

    force_needed = GetForceNeeded(begin, end)
    print(force_needed)


# current_position = 1

# max_force = GetForceNeeded(current_position, current_position+1)

# current_position += 1

# while current_position != num_of_stones:
#     force_to_next_step = GetForceNeeded(current_position, current_position+1)

#     if max_force < force_to_next_step:
#         max_force = force_to_next_step

#     current_position += 1

# print(max_force)


#@@@@@@
# 1번 돌부터 step가능한 다음 돌로 이동해본다
# 이동할때 든 힘을 비교하고 시나리오별 max 값을 갱신
# 오른쪽에 도달했으면 max값을 answer에 append

# 오른쪽에 도달한경 우 중 max값이 가장 적은 값을 리턴한다.

# try( current, max )
#     return -1 or max
