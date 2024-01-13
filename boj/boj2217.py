import sys

def GetPartialSum():
    global rope_total_count
    global rope_list_sorted
    global index

    if index < len(rope_list_sorted)-1:
        while rope_list_sorted[index] == rope_list_sorted[index+1]:
            index+=1
            if index == len(rope_list_sorted)-1:
                break
    sum = rope_list_sorted[index] * (index+1)


    # print("index:", index)
    # print("list[%d]:%d"%(index, rope_list_sorted[index]))
    # print("sum = index[%d] * min[%d]" % ( index+1, rope_list_sorted[index]))

    return sum


rope_total_count = int(sys.stdin.readline().rstrip())

input_list = list()

for i in range(rope_total_count):
    temp = int(sys.stdin.readline().rstrip())
    input_list.append(temp)


rope_list_sorted = sorted(input_list, reverse=True)

partial_sum = 0
index = 0
answer = 0
while True:
    if index == len(rope_list_sorted):
        break
    partial_sum = GetPartialSum()
    index+=1

    if answer < partial_sum:
        answer = partial_sum 

print(answer)
