import sys

N, M = list(map(int, sys.stdin.readline().split()))


array_input = list(map(int, sys.stdin.readline().split()))
array_sum = [0 for _ in range(N)]


for i in range(N):
    if i == 0:
        array_sum[i] = array_input[i]
    else:
        array_sum[i] = array_sum[i-1] + array_input[i]
    

for j in range(M):
    nums_input = list(map(int, sys.stdin.readline().split()))

    num_begin=nums_input[0] -1
    num_end=nums_input[1] -1
    num_sum = array_sum[num_end] - array_sum[num_begin]

    print(num_sum + array_input[num_begin])
