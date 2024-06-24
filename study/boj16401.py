num_of_kids, num_of_stick = list(map(int, input().split()))

#print(num_of_kids, num_of_stick)

stick_array = list()

input_list = list(map(int,input().split()))
stick_array = input_list.copy()

stick_array.sort()

# print(input_list)
# print(stick_array)

#가장 큰 크기부터 스틱 개수 세서, 조카들 수보다 작은지 확인한다.
def CanDistributeWithlength(_stick_length:int):
    global stick_array
    global num_of_kids
    count = 0
    for i in range(len(stick_array)):
        if stick_array[-1-i] >= _stick_length:
            count+=1
            if count==num_of_kids:
                return 1
        else:
            break
    
    return 0

#print(CanDistributeWithlength(8))

#못하면 나눈다.
def SplitLongestStick():
    global stick_array
    longest_length = stick_array[-1]
    if (longest_length//2 == 0):
       stick_array.append(longest_length//2) 
       stick_array.append(longest_length//2) 
    else:
       stick_array.append(longest_length//2) 
       stick_array.append(longest_length//2 + 1) 

    stick_array.remove(longest_length)
    stick_array.sort()
        


trying_cursor = len(stick_array)-1

answer = 0

while trying_cursor != -1:
    if CanDistributeWithlength(stick_array[trying_cursor]):
        #answer.append(stick_array[trying_cursor])
        answer = stick_array[trying_cursor]
        break

    if trying_cursor == 0:
        SplitLongestStick()
        trying_cursor = len(stick_array)-1
        continue

    trying_cursor -= 1

print(answer)



def GetBiggestSticks():
    return 0

