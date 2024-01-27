
row, col = list(map(int, input().split()))


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
matrix_diff = [[0 for _ in range(col)] for _ in range(row)]
for row_index in range(row):
    for col_index in range(col):
        if (matrix_a[row_index][col_index] == matrix_b[row_index][col_index]):
            matrix_diff[row_index][col_index] = 0
        else:
            matrix_diff[row_index][col_index] = 1
        #matrix_diff[row_index][col_index] = (matrix_a[row_index][col_index] == matrix_b[row_index][col_index])

for i in range(row):
    print(matrix_diff[i])


#