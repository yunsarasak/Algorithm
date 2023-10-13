N, M = list(map(int, input().split()))

num_list = list(map(int, input().split()))

sum_list = list()

sum_list.append(num_list[0])

for loop_index in range(N -1):
    sum_list.append(sum_list[loop_index] + num_list[1 + loop_index])

for loop in range(M):
    sum = 0

    i, j = list(map(int, input().split()))

    i -= 2
    j -= 1

    #for k in range(j - i + 1):
    #    #print("adding" , num_list[i + k])
    #    sum += num_list[i + k]
    
    #print(sum)
    print(sum_list[j] , sum_list[i])
    answer = sum_list[j] - sum_list[i]
    print(answer)

