
row, col = list(map(int, input().split()))

def IsSameMatrix( ):
    global row, col
    global matrix_a, matrix_b
    
    if matrix_a == matrix_b:
        # print("same")
        return True
    else:
        # print("not same")
        return False

def Reverse( matrix_to_reverse, _row_index, _col_index):
    global row, col

    for i in range(3):
        for j in range(3):
            if matrix_to_reverse[_row_index+i][_col_index+j] == '1':
                matrix_to_reverse[_row_index+i][_col_index+j] = '0'
            else:
                matrix_to_reverse[_row_index+i][_col_index+j] = '1'

                


matrix_a = [[0 for _ in range(col)] for _ in range(row)]
matrix_b = [[0 for _ in range(col)] for _ in range(row)]
# A, B 구분 해서 입력 받는다.
for row_index in range(row*2):
    temp = input()
    if row_index < row:
        for col_index in range(col):
            matrix_a[row_index][col_index] = temp[col_index]
    else:
        for col_index in range(col):
            matrix_b[row_index - row][col_index] = temp[col_index]
        

# print(matrix_a)
# print("@@@@@@@@@")
# print(matrix_b)


# A, B 다른 부분을 구함 ( 각 원소를 xor )
# matrix_diff = [[0 for _ in range(col)] for _ in range(row)]
# for row_index in range(row):
#     for col_index in range(col):
#         if (matrix_a[row_index][col_index] == matrix_b[row_index][col_index]):
#             matrix_diff[row_index][col_index] = 0
#         else:
#             matrix_diff[row_index][col_index] = 1
#         #matrix_diff[row_index][col_index] = (matrix_a[row_index][col_index] == matrix_b[row_index][col_index])

# for i in range(row):
#     print(matrix_diff[i])

reverse_count = 0

# print("row_index:", row_index)
# print("col_index:", col_index)
# print("row:", row)
# print("col:", col)
for row_index in range(row - 2):
    for col_index in range(col - 2):
        if matrix_a[row_index][col_index] != matrix_b[row_index][col_index]:
            Reverse(matrix_a, row_index, col_index)
            reverse_count += 1
        else:
            continue

# print("result")
if IsSameMatrix():
    print(reverse_count)
else:
    print("-1")
