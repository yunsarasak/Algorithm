import sys

N, M = list(map(int,sys.stdin.readline().split()))

matrix = list()

for row_index in range(N):
    temp = list(map(int, sys.stdin.readline().split()))
    matrix.append(temp)


from_to_lists = list()

for _ in range(M):
    from_to_list = list(map(int, sys.stdin.readline().split()))
    from_to_lists.append(from_to_list)


def GetDPArray(_from_x, _from_y, _to_x, _to_y):
    global array_to_add
    global matrix 
    sum = 0
    
    for row_index in range(_from_x, _to_x+1):
        for col_index in range(_from_y, _to_y+1):
            print("appending %d"%matrix[row_index][col_index])
            array_to_add.append(matrix[row_index][col_index])

FROM_X = 0
FROM_Y = 1
TO_X = 2
TO_Y = 3


for test_case in range(M):
    print("case %d"%test_case)
    array_to_add = list()
    array_dp = [0 for i in range(N)]

    from_x = from_to_lists[test_case][FROM_X] -1
    from_y = from_to_lists[test_case][FROM_Y] -1
    to_x = from_to_lists[test_case][TO_X] -1
    to_y = from_to_lists[test_case][TO_Y] -1
    print("%d %d %d %d"% (from_x, from_y, to_x, to_y))
    GetDPArray(from_x, from_y, to_x, to_y)

    print(array_to_add)

    array_dp[0] = array_to_add[0]

    for i in range(1, N):
        print("i:",i)
        array_dp[i] = array_dp[i-1] + array_to_add[i]

    answer = array_dp[-1]

    print()
    print(answer)
