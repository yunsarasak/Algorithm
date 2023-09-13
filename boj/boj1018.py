#2차원 배열로 나와있지만 사실은 BWBW... 이나 WBWB... 로 반복되는 배열에서 틀린 개수 찾는 문제로 단순화할 수 있다.
#고!! 생각했는데, WBWB, BWBW만 반복되는게 아니라 행이 바뀌면 마지막 색이 반복된다는 점을 간과함.
#그래서 최종 목표인 보드의 색 배치를 아래에 정의해서 사용했음.

# Black을 B, 0으로
# White를 W, 1으로 표시한다.

#well aligned board
blackBoard = [0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0]
whiteBoard = [1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1]



#print("bboard count", len(blackBoard))

#worst case
globalMin = 32

#8x8 기준 배열과 틀린 개수 세기
def CountIncorrect( _listA:list, _listB:list ):
    count = int(0)
    for i in range( 8 * 8 ):
        if ( _listA[i] != _listB[i] ):
            count+=1
        #else:
            #print("%d 번째" % i, end="")
            #print(_listA[i], _listB[i])
            
    return count


row, col = list(map(int, input().split()))

matrix = list()

for i in range(row):
    matrix.append(input())

#print()

"""
for i in range(row):
    print(matrix[i])
"""

#8x8 고르기 ( 0,0 ~ row-8, col-8 )
def SelectBoard(_x:int, _y:int):
    ret = list()
    
    for row_index in range(_x, _x + 8):
        for col_index in range(_y, _y + 8):
            ret.append(0 if matrix[row_index][col_index]=='B' else 1)
    
    return ret

#for debugging
rectCount = 0

for ri in range(0, row - 8 + 1):
    for ci in range(0, col - 8 + 1):
        #print("row", ri, "col", ci)
        boardSelected = SelectBoard(ri, ci)
        #print(boardSelected)
        rectCount+=1


        #8x8 기준 배열과 틀린 개수 세기
        #둘중 적은수를 현재 구역에서의 최소 값으로 저장
        localMin = min( CountIncorrect(blackBoard, boardSelected), CountIncorrect(whiteBoard, boardSelected))

        #현재 구역의 최소값이 전체 구역의 최소값보다 작다면 전체 구역의 최소값 갱신
        if localMin < globalMin:
            globalMin = localMin
#print(rectCount)

print(globalMin)