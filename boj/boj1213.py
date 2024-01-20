def GetPalindrome(_character_dicts, _center_string):
    # 오름차순으로 1/2개씩 프린트
    if _center_string == None:
        return "I'm Sorry Hansoo"

    returning_string = str()
    first_half_string = str()
    
    for i in _character_dicts:
        first_half_string += i*(_character_dicts[i] // 2)

    last_half_string_list = list(first_half_string)

    last_half_string_list.reverse()
    last_half_string = ''.join(last_half_string_list)

    returning_string = first_half_string + _center_string + last_half_string

    return returning_string

    
        

input_string = input()

character_dicts = dict()

for character in range(ord('A'), ord('Z')+1):
    character_dicts[chr(character)] = 0

for input_character in input_string:
    character_dicts[input_character] += 1


odd_count_character = list()

# get center
for character in character_dicts:
    if character_dicts[character] % 2 == 1:
        odd_count_character.append(character)

#print("odd char : ", odd_count_character)
if len(odd_count_character) == 0:
    # 가장 뒤에 있는 문자가 모두가 cneter
    for i in character_dicts:
        center_character = i
        if character_dicts[i] == 0:
            break
    center_string = center_character*character_dicts[center_character]
elif len(odd_count_character) == 1:
    # 하나 더 많은 문자가 중간으로
    center_character = odd_count_character[0]
    character_dicts[center_character] -= 1
    center_string = center_character
else:
    # 만들 수 없음
    center_string = None

answer = GetPalindrome(character_dicts, center_string)

print(answer)