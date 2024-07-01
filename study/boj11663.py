N, M = list(map(int,input().split()))

list_points =list()

def GetIndex(_target:int):
    global list_points
    left = 0
    right = len(list_points) - 1

    #맨 처음, 양 끝 값을 넘어가는지 확인
    if _target <= list_points[0]:
        return 0
    elif _target >= list_points[-1]:
        return len(list_points)-1

    while (right - left) > 1:
        mid = (right + left)//2

        if list_points[mid] > _target:
            right = mid
        elif list_points[mid] < _target:
            left = mid
        else:
            #target == list_points[mid]
            break
        
    return mid


def CountPoints(_begin:int, _end:int):
    global list_points
    #begin 보다 작거나 같은 값중 가장 큰 값
    b_index = GetIndex(_begin)
    # print("%d보다 작거나 같은 값중 가장 큰 값은 %d"%(_begin,list_points[b_index]))
    
    #end 보다 크거나 같은 값중 가장 작은 값
    e_index = GetIndex(_end)
    # print("%d보다 크거나 같은 값중 가장 작은 값은 %d"%(_end,list_points[e_index]))

    #index 차이를 구하기 ( 개수 )
    point_included = e_index - b_index

    #포함 여부 판단
    if list_points[b_index] >= _begin:
        point_included += 1

    if list_points[e_index] <= _end:
        point_included += 1

    return point_included


list_points = list(map(int,input().split()))

#print(list_points)
list_points.sort()
#print(list_points)



answer = list()

for i in range(M):
    begin, end = list(map(int, input().split()))
    
    answer.append(CountPoints(begin, end))


# GetIndex(9)

# GetIndex(10)

# GetIndex(11)

# print(answer)
for i in answer:
    print(i - 1)