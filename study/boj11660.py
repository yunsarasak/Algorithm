import sys
#https://www.acmicpc.net/problem/11660

# N * N 행렬에서
# M 개만큼 개수 구하기

N, M = list(map(int,sys.stdin.readline().split()))

# init matrix
matrix_sum = []
matrix_input = []

for i in range(N):
    # 한 행을 입력받음
    array_input = list(map(int, sys.stdin.readline().split()))

    # 누적합 초기화
    array_sum = [0 for _ in range(N)]

    for j in range(N):
        #만약 첫번째아이템이면 입력을 그대로 누적합으로 계산
        if j == 0:
            array_sum[j] = array_input[j]
        #아니면 이전 누적합에다가 더함
        else:
            array_sum[j] = array_sum[j-1] + array_input[j]
    
    #입력받은 행과, 누적합을 행렬변수에 기록
    matrix_input.append(array_input)
    matrix_sum.append(array_sum)


# 시작점 ~ 끝점까지의 합을 구하는 함수
def SumFromTo(from_x, from_y, to_x, to_y):
    global matrix_sum
    global matrix_input

    # 리턴 값 초기화
    sum = 0

    for row_index in range(from_x, to_x+1):
        # 행 단위로 누적합을 계산
        sum += matrix_sum[row_index][to_y] - matrix_sum[row_index][from_y]

        # 누적합을 기록한 행의 제일 오른쪽 값에서 왼쪽 값을 빼게되면 제일 왼쪽값은 합에서 제외되므로,
        # 해당 값을 리턴값에 추가함.
        # ex)       sum3 : a1 + a2 + a3
        #           sum1 : a1
        #    sum3 - sum1 :      a2 + a3
        sum += matrix_input[row_index][from_y]

    return sum

answer_list = []

for _ in range(M):
    from_x, from_y, to_x, to_y = list(map(int,sys.stdin.readline().split()))

    # 인덱스가 0부터 시작하는데 반해,
    # 입력되는 인덱스가 1부터 시작되므로
    # 값을 조정함
    from_x -= 1
    from_y -= 1
    to_x -= 1
    to_y -= 1

    answer = SumFromTo(from_x, from_y, to_x, to_y)

    answer_list.append(answer)

for m in range(M):
    print(answer_list[m])