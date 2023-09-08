#https://codeup.kr/problem.php?id=4818

def PartialResult(_row :int, _col :int):
    if(_row == 0 or _col == 0):
        return 1
    else:
        return PartialResult(_row-1, _col) + PartialResult(_row, _col-1)

#read input
#n for row
#m for column
n, m, target = list(map(int, input().split()))

if (target == 0):
    target = m * n

#get target row ( share )
target_row = ((target) // (m))
mod = target % m

if(mod == 0):
    target_row -= 1

#get target col ( remainder )
target_col = target - ( target_row * m ) - 1

#DEBUG
#print( "row, col = ", target_row, target_col, sep = " ")

#sol1. set matrix
#set matrix for start to target ( 0, 0) -> ( target row, target col)
#set matrix for target to end ( target row, target col) -> ( n, m)

#sol2. recursive
#get partial results multiplied
resultToTarget = PartialResult( target_row, target_col )
resultToEnd = PartialResult( n - (target_row+1), m - (target_col+1) )

#DEBUG
#print("to the target : ", resultToTarget)
#print("to the end : ", resultToEnd)

result = resultToTarget * resultToEnd

print(result)