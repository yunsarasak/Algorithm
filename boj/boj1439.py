
def DoesCurrentBitEqualToPrevious():
    global bit
    global bit_previous
    # print("cur:", bit, "prev", bit_previous)
    if bit == bit_previous:
        # print("same")
        return True
    else:
        # print("not")
        return False


S = input()

reverse_count = 0
first_flag = True

for bit in S:
    if first_flag == True:
        bit_previous = bit
        first_flag = False

    if DoesCurrentBitEqualToPrevious():
        continue
    else:
        reverse_count += 1
        bit_previous = bit

# print("total reverse count :", reverse_count)
if reverse_count == 1:
    answer = 1
else:
    answer = (reverse_count//2) + (reverse_count%2)

print(answer)