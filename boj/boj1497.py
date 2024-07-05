num_of_guitar, num_of_songs = list(map(int, input().split()))

def StringToDecimal(_str:str):
    #convert Y to 1, N to 0

    string_length = len(_str)
    binary_list = [0 for _ in range(string_length)]

    cursor = 0

    for i in _str:
        if i == "Y":
            binary_list[cursor] = '1'
            cursor+=1
        else:
            binary_list[cursor] = '0'
            cursor+=1

    binary_string = ''.join(binary_list)

    return_decimal = int(binary_string, 2)

    return return_decimal

guitar_table = list()

#print()

for i in range(num_of_guitar):
    name_of_guitar, song_playable = list(map(str, input().split()))

    guitar_table.append((name_of_guitar, StringToDecimal(song_playable)))
    # print(name_of_guitar, StringToDecimal(song_playable))


#전체를 or 하면 최대 곡 수가 나옴
highst_number_of_songs = 0

for tuple in guitar_table:
    highst_number_of_songs = highst_number_of_songs | tuple[1]

def GetCountOfGuitar():
    global highst_number_of_songs, guitar_table, num_of_guitar

    if highst_number_of_songs == 0:
        return -1
    
    #내림차순을 만들어서 가장 큰 수부터 뺀다.
    guitar_table = sorted(guitar_table, key=lambda item: item[1], reverse=True)

    cursor = 0
    count = 0

    while (highst_number_of_songs != 0) and (cursor <= num_of_guitar-1):
        # print(cursor)
        if (highst_number_of_songs - guitar_table[cursor][1])>= 0:
            count+=1
            highst_number_of_songs -= guitar_table[cursor][1]
        cursor+=1

    
    return count

answer = GetCountOfGuitar()

print(answer)


#print(highst_number_of_songs)