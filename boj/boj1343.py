input_string = input()


def GetRemainXLength(_index):
    global input_string
    global string_length

    # print("index:", _index)

    i =0
    if input_string[_index + i] == '.':
        return -1

    while input_string[_index + i] == 'X':
        if string_length == _index + i + 1:
            i+=1
            break
        if i == 4:
            break
        i+=1

    # print("remain : %d"% i)
    return i
        
def SetPolyomino(_index,_character):
    global output_string
    if _character == 'A':
        for i in range(4):
            output_string[_index + i] = 'A'
    else:
        for i in range(2):
            output_string[_index + i] = 'B'
    
    return
        
    

# print(input_string)
string_length = len(input_string)
output_string = list(input_string)

answer = 0

i = 0
while i != string_length:
    #print(i)
    #Get remain X
    if i == string_length:
        break
    remain_length = GetRemainXLength(i)
    #print("remain:",remain_length)

    if remain_length == 4:
        SetPolyomino(i, 'A')
        # print("output: ", output_string)
        i += 4
    elif remain_length == 2:
        SetPolyomino(i, 'B')
        # print("output: ", output_string)
        i += 2
    elif remain_length == -1:
        i += 1
    else:
        answer = -1
        break
        
        

if answer == -1:
    print(answer)
else:
    print(''.join(output_string))