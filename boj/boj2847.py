import sys
#import time


num_count = int(input())

min = 20001

input_arr = [0 for i in range(num_count+1)]

for i in range(num_count):
    temp = int(sys.stdin.readline())

    input_arr[i] = temp

    if min >= temp:
        # print("%d > %d"% (min, temp))
        min = temp
        min_index = i


# print(input_arr)
# print("min: ",min_index)

backward_index = min_index
forward_index = min_index
score_change_count = 0

while backward_index:
    backward_index-=1
    while input_arr[backward_index] >= input_arr[backward_index + 1]:
        #print("arr[%d] : %d -> %d"%(backward_index, input_arr[backward_index], input_arr[backward_index] -1))
        input_arr[backward_index] -= 1
        score_change_count += 1


while forward_index != num_count -1:
    forward_index+=1
    while input_arr[forward_index] <= input_arr[forward_index - 1]:
        #print("input_arr[forward_index]%d <= input_arr[forward_index-1]%d"%(input_arr[forward_index], input_arr[forward_index-1]))
        #print("forward arr[%d] : %d -> %d"%(forward_index, input_arr[forward_index], input_arr[forward_index]-1))
        #time.sleep(1)
        input_arr[forward_index] += 1
        score_change_count += 1

# while forward_index != num_count -1:
#     forward_index += 1
#     if forward_index == num_count:
#         break
#     while input_arr[forward_index] != input_arr[forward_index - 1] + 1:
#         print("forward arr[%d] : %d -> %d"%(forward_index, input_arr[forward_index], input_arr[forward_index]-1))
#         input_arr[forward_index] += 1
#         score_change_count += 1
    

print(score_change_count)