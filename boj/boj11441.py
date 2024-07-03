N = int(input())

sum = 0

def MyInt(_str:str):
    global sum

    sum = sum+int(_str)
    return sum

def GetActualValue(_index:int):
    global accumulated_list

    if _index == 0:
        return accumulated_list[_index]
    else:
        return accumulated_list[_index] - accumulated_list[_index-1]


accumulated_list = list(map(MyInt, input().split()))
#print(accumulated_list)

M = int(input())

answer = list()

for i in range(M):
    begin, end = list(map(int, input().split()))

    begin -= 1
    end -= 1

    partial_answer = accumulated_list[end] - accumulated_list[begin] + GetActualValue(begin)
    #print(partial_answer)
    answer.append(partial_answer)


for i in answer:
    print(i)

    