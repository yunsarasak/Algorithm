#read input
def PrintPalindrome():
    global aligned_dicts
    global character_to_be_cnetered
    global input_string
    global character_dicts

    center_index = len(input_string)//2 - character_dicts[character_to_be_cnetered]//2
    cursor_index = 0

    return_string = str()
    first_half = str()

    
    for i in aligned_dicts:
        if i[0] == character_to_be_cnetered:
            continue
        if cursor_index == center_index:
            break
            # cursor_index += character_dicts[character_to_be_cnetered]
        first_half += i[0]*(character_dicts[i[0]]//2)
        cursor_index += (character_dicts[i[0]]//2)

        # print(cursor_index)
    
    return_string += first_half + character_to_be_cnetered*character_dicts[character_to_be_cnetered]
    first_half_list = list(first_half)
    first_half_list.reverse()
    last_half = ''.join(first_half_list)
    return_string += last_half
    
    print(center_index)

    return return_string

input_string = input()

character_dicts = dict()

for character in range(ord('A'), ord('Z')+1):
    character_dicts[chr(character)] = 0

for input_character in input_string:
    character_dicts[input_character] += 1


odd_count = 0

answer = 0

#check can be
for character in character_dicts:
    # count odd 
    # if two or more odd, break
    if character_dicts[character] % 2 != 0:
        odd_count += 1
        character_to_be_cnetered = character
        if odd_count > 1:
            answer = -1
            break

if answer == -1:
    print(answer)
else:
    aligned_dicts = sorted(character_dicts.items(), key=lambda item:item[0])
    print(PrintPalindrome())



#align

#make answer