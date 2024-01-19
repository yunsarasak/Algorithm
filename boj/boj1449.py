error_count, tape_length = list(map(int, input().split()))

#print(error_count, tape_length)
tape_count = 0

def PatchTape(index, length):
    global error_position

    for i in range(length):
        if index+i > 1000:
            break
        #print("set index+i(%d) to 0"%(index+i))
        error_position[index + i] = 0
    
    return

error_list = list(map(int, input().split()))

error_position = [0 for _ in range(1001)]

for i in error_list:
    error_position[i] = 1

cursor = 1
while cursor < 1001:
    if error_position[cursor] == 1:
        tape_count += 1
        #print("patch %d"%cursor)
        PatchTape(cursor, tape_length)
    cursor += 1
    

print(tape_count)

