
correct_array = list()

# which is answer
green_light = 0
yellow_light = 0


for row_index in range(3):
    temp_row = list(input().strip())
    correct_array.append(temp_row)

guessing_array = list()

for row_index in range(3):
    temp_row = list(input().strip())
    guessing_array.append(temp_row)

# for row_index in range(3):
#     for col_index in range(3):
#         print(guessing_array[row_index][col_index], sep="", end="")
#     print()

def IsThere(_row, _col):
    global correct_array
    global guessing_array
    is_there = 0

    for row in range(3):
        for col in range(3)ㅏ
            if guessing_array[_row][_col] == correct_array[row][col]:
                correct_array[row][col] = '0'
                is_there = 1
                return is_there

    return is_there


# check green
for row_index in range(3):
    for col_index in range(3):
        if guessing_array[row_index][col_index] == correct_array[row_index][col_index]:
            green_light += 1
            guessing_array[row_index][col_index] = '0'
            correct_array[row_index][col_index] = '0'

# check yellow
for row_index in range(3):
    for col_index in range(3):
        if guessing_array[row_index][col_index] == '0':
            continue
        yellow_light += IsThere(row_index, col_index)


        


print(green_light)
print(yellow_light)
