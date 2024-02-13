import sys
#https://www.acmicpc.net/problem/11660

# N * N 행렬에서
# M 개만큼 개수 구하기

N, M = list(map(int,sys.stdin.readline().split()))

matrix = list()

for row_index in range(N):
    temp = list(map(int, sys.stdin.readline().split()))
    matrix.append(temp)

# for row_index in range(N):
#     print( matrix[row_index])

from_to_lists = list()
for _ in range(M):
    from_to_list = list(map(int, sys.stdin.readline().split()))

    from_to_lists.append(from_to_list)

FROM_X = 0
FROM_Y = 1
TO_X = 2
TO_Y = 3

# for i in range(M):
#     print( from_to_lists[i] )
#     from_x = from_to_lists[i][FROM_X]
#     from_y = from_to_lists[i][FROM_Y]
#     to_x = from_to_lists[i][TO_X]
#     to_y = from_to_lists[i][TO_Y]
#     print("from(%d, %d)"%(from_x, from_y), "to(%d, %d)"%(to_x, to_y) )

test_case = 0

# def IsIncluded(_row_index, _col_index):
#     global from_to_lists
#     global test_case

def SumFromTo(_from_x, _from_y, _to_x, _to_y):
    global matrix

    sum = 0
    
    for row_index in range(_from_x, _to_x+1):
        for col_index in range(_from_y, _to_y+1):
            #print("adding%d [%d][%d]" %(matrix[row_index][col_index], row_index, col_index))
            sum += matrix[row_index][col_index]

    return sum


answer = list()
for test_case in range(M):
    from_x = from_to_lists[test_case][FROM_X] -1
    from_y = from_to_lists[test_case][FROM_Y] -1
    to_x = from_to_lists[test_case][TO_X] -1
    to_y = from_to_lists[test_case][TO_Y] -1
    partial_answer = SumFromTo(from_x, from_y, to_x, to_y)
    print(partial_answer)
    
    answer.append(sum)
