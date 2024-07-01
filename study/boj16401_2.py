from sys import stdin
#n = int(stdin.readline())

num_of_kids, num_of_stick = list(map(int, stdin.readline().split()))


#print(num_of_kids, num_of_stick)

stick_array = list()

input_list = list(map(int,stdin.readline().split()))
stick_array = input_list.copy()

stick_array.sort()

# print(input_list)
# print(stick_array)

def GetPossibleCount(_stick_length:int):
    global stick_array
    global num_of_stick
    count = 0
    
    for i in num_of_stick:
        if stick_array[i] >= _stick_length:
            count+=1

    return count


#가장 큰 크기부터 스틱 개수 세서, 조카들 수보다 작은지 확인한다.
def CanDistributeWithlength(_stick_length:int):
    global stick_array
    global num_of_kids

    possible_count = GetPossibleCount(_stick_length)

    if possible_count >= num_of_kids:
        return 1
    else:
        return -1

#print(CanDistributeWithlength(8))

left = 1
right = stick_array[num_of_stick-1]


answer = 0

while left < right:
    trying_cursor = (left + right)//2
    next_move = CanDistributeWithlength(trying_cursor)

    if next_move == 1:
        left += 1
        answer = trying_cursor
    elif next_move == -1:
        right -= 1

print(answer)
