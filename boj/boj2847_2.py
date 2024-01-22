import sys

arr_len = int(input())

num_array = [ 0 for _ in range(arr_len)]

for i in range(arr_len):
    num_array[i] = int(sys.stdin.readline())

index = arr_len-1
change_count = 0

while index:
    if index == 0:
        break
    while num_array[index] <= num_array[index-1]:
        num_array[index-1] -= 1
        change_count+=1
    index-=1


print(change_count)
